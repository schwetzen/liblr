from django.contrib.auth import mixins
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.utils import timezone

from functools import reduce
from operator import or_ as combine

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

        url = request.POST.get('next', 'tips')
        params = ['{key}={data}'.format(key=k, data=data.get(k)) for k in ('filter', 'search',) if data.get(k)]

        if params:
            url += '?' + '&'.join(params)

        return redirect(url)

    def delete(self, request, tip_id):
        tip = self.get_tip(request, tip_id)
        tip.is_deleted = True
        tip.save()
        return redirect('tips')


class ReadingTipListView(mixins.LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    template_name = 'reading_tip_list.html'

    def filter_options(self):
        return (
            ('', 'All'),
            ('read', 'Read'),
            ('unread', 'Unread'),
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        query = self.request.GET.get('search', None)
        context.update(title='Search | {q}'.format(q=query) if query else 'Tips')
        context.update(search=query)
        return context
    
    def get_queryset(self):
        authorized = Q(user=self.request.user) & Q(is_deleted=False)
        queryset = ReadingTip.objects.filter(authorized)

        filter_key = self.request.GET.get('filter', None)
        if filter_key:
            queryset = queryset.filter(has_been_read=filter_key == 'read')

        query = self.request.GET.get('search', None)
        if query:
            contains = lambda w: Q(title__icontains=w) | Q(description__icontains=w)
            queryset = queryset.filter(reduce(combine, map(contains, query.split())))

        return queryset.order_by('-id')

    def get(self, request, *args, **kwargs):
        if 'export' not in request.GET:
            return super().get(request, *args, **kwargs)

        import csv

        tips = self.get_queryset().all()
        filename = 'tips {zone}'.format(zone=timezone.now())

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{f}.csv"'.format(f=filename)

        writer = csv.writer(response)
        header = ('Type', 'Title', 'ISBN', 'URL', 'Description',)
        rows = list(map(ReadingTip.export_fields, tips))
        writer.writerows((header, *rows))

        return response


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
            start_date=tip.start_date,
            end_date=tip.end_date,
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
                tip.start_date = data.get('start_date', tip.start_date)
                tip.end_date = None if not tip.start_date else data.get('end_date', tip.end_date)
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
