from django.views import generic
from django.contrib.auth import mixins
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from app.models import ReadingTip
from app.forms import ReadingTipCreateForm


class ReadingTipListView(mixins.LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    template_name = 'reading_tip_list.html'

    def get_queryset(self):
        return ReadingTip.objects.filter(user=self.request.user).order_by('-id')


class ReadingTipCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    login_url = reverse_lazy('login')
    form_class = ReadingTipCreateForm
    template_name = 'reading_tip_form.html'

    def post(self, request, *args, **kwargs):
        form = ReadingTipCreateForm(self.request.POST)

        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        ReadingTip.objects.create(user=self.request.user, **form.cleaned_data)

        return redirect('tips')
