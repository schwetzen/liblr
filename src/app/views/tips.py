from django.views import generic
from django.views.generic.edit import DeleteView
from django.contrib.auth import mixins
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from app.models import ReadingTip
from app.forms import ReadingTipCreateForm


class ReadingTipListView(mixins.LoginRequiredMixin, generic.ListView):
    login_url = reverse_lazy('login')
    template_name = 'reading_tip_list.html'

    def post(self, request, tip_id):
        tip = ReadingTip.objects.get(id=tip_id)
        tip.has_been_read = 'mark_as_read' in request.POST
        tip.save()

        return redirect('tips')

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


class ReadingTipDeleteView(DeleteView):
    model = ReadingTip
    success_url = reverse_lazy('tips')

    def delete(self, request, pk):
        tip = ReadingTip.objects.get(id=pk)
        tip.is_deleted = True
        tip.save()
        return redirect('tips')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)





