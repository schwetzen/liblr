from django.contrib.auth import mixins
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseServerError
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from functools import reduce
import operator

from app.forms import ReadingTipCreateForm, ReadingTipUpdateForm
from app.models import ReadingTip, ReadingTipContentBook, ReadingTipContentWebsite
from app.views.dispatch import DispatchView


class ReadingTipView(mixins.LoginRequiredMixin, DispatchView):
    login_url = reverse_lazy('login')
    template_name = 'reading_tip.html'

    def get_tip(self, request, tip_id):
        return get_object_or_404(
            ReadingTip,
            id=tip_id,
            user=request.user,
            is_deleted=False
        )

    def get(self, request, tip_id):
        tip = self.get_tip(request, tip_id)
        return render(request, self.template_name, {'tip': tip})

    def patch(self, request, tip_id):
        tip = self.get_tip(request, tip_id)
        data = request.POST

        if 'has_been_read' in data:
            tip.has_been_read = bool(data.get('has_been_read'))

        tip.save()
        return redirect(request.POST.get('next', 'tips'))

    def delete(self, request, tip_id):
        tip = self.get_tip(request, tip_id)
        tip.is_deleted = True
        tip.save()
        return redirect('tips')


class ReadingTipListView(mixins.LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    template_name = 'reading_tip_list.html'

    def get_queryset(self):
        q = Q(user=self.request.user) & Q(is_deleted=False)
        return ReadingTip.objects.filter(q).order_by('-id')

    def post(self, request, tip_id):
        tip = ReadingTip.objects.get(id=tip_id)
        tip.has_been_read = 'mark_as_read' in request.POST
        tip.save()
        return redirect('tips')


class ReadingTipSearchListView(ReadingTipListView):
    def get_queryset(self):
        result = super(ReadingTipSearchListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.or_, (Q(title__icontains=word) for word in query_list)) |
                reduce(operator.or_, (Q(description__icontains=word) for word in query_list))
            )
        return result


class ReadingTipCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    form_class = ReadingTipCreateForm
    template_name = 'reading_tip_form.html'

    def post(self, request, *args, **kwargs):
        form = ReadingTipCreateForm(self.request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        data = form.cleaned_data

        isbn = data.pop('isbn', None)
        url = data.pop('url', None)

        try:
            with transaction.atomic():
                tip = ReadingTip.objects.create(user=self.request.user, **data)

                # TODO: Fix
                if tip.content_type is ReadingTip.BOOK:
                    ReadingTipContentBook.objects.create(
                        tip=tip,
                        isbn=isbn
                    )

                elif tip.content_type is ReadingTip.WEBSITE:
                    ReadingTipContentWebsite.objects.create(
                        tip=tip,
                        url=url
                    )

        except:
            return HttpResponseServerError('Whoopsie')

        return redirect('tips') if not tip else redirect('tip', tip_id=tip.id)


class ReadingTipUpdateView(mixins.LoginRequiredMixin, DispatchView):
    login_url = reverse_lazy('login')
    template_name = 'reading_tip_form.html'

    def get_tip(self, request, tip_id):
        return get_object_or_404(
            ReadingTip,
            id=tip_id,
            user=request.user,
            is_deleted=False
        )

    def get_form(self, tip):
        data = dict(
            title=tip.title,
            description=tip.description,
            isbn=None if tip.content_type is not ReadingTip.BOOK else tip.content().isbn,
            url=None if tip.content_type is not ReadingTip.WEBSITE else tip.content().url,
        )
        form = ReadingTipUpdateForm(data)

        # TODO: Fix
        if tip.content_type is ReadingTip.BOOK:
            del form.fields['url']

        elif tip.content_type is ReadingTip.WEBSITE:
            del form.fields['isbn']

        return form

    def get(self, request, tip_id):
        tip = self.get_tip(request, tip_id)
        form = self.get_form(tip)

        return render(request, self.template_name, {'form': form, 'tip': tip})

    def patch(self, request, tip_id):
        tip = self.get_tip(request, tip_id)
        form = ReadingTipUpdateForm(request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form, 'tip': tip})

        data = form.cleaned_data

        isbn = data.pop('isbn', None)
        url = data.pop('url', None)

        try:
            with transaction.atomic():
                tip.title = data.get('title', tip.title)
                tip.description = data.get('description', tip.description)
                tip.save()

                # TODO: Fix
                if tip.content_type is ReadingTip.BOOK and isbn:
                    ReadingTipContentBook.objects.create(
                        tip=tip,
                        isbn=isbn
                    )

                elif tip.content_type is ReadingTip.WEBSITE and url:
                    ReadingTipContentWebsite.objects.create(
                        tip=tip,
                        url=url
                    )

        except:
            return HttpResponseServerError('Whoopsie')

        return redirect('tip', tip_id=tip.id)
