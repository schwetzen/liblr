from django.views import generic
from django.shortcuts import redirect
from app.forms.readingtip import ReadingTipCreateForm


class ReadingTipCreate(generic.CreateView):
    form_class = ReadingTipCreateForm
    template_name = 'reading_tip_form.html'

    def post(self, request, *args, **kwargs):
        form = ReadingTipCreateForm(self.request.POST)
        if form.is_valid():
            form.save()

        return redirect('tips')
