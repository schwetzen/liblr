from django.views import generic
from django.shortcuts import redirect
from app.models import ReadingTip
from app.forms import ReadingTipCreateForm


class ReadingTipListView(generic.ListView):
    template_name="reading_tip_list.html"

    def get_queryset(self):
        return ReadingTip.objects.all()


class ReadingTipCreateView(generic.CreateView):
    form_class = ReadingTipCreateForm
    template_name = 'reading_tip_form.html'

    def post(self, request, *args, **kwargs):
        form = ReadingTipCreateForm(self.request.POST)

        if form.is_valid():
            form.save()

        return redirect('tips')
