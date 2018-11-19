from django.views.generic.list import ListView
from app.models.tip import ReadingTip

class TipsView(ListView):
    template_name="tips.html"

    def get_queryset(self):
        return ReadingTip.objects.all()

