from django.views.generic.list import ListView
from django.http import HttpResponseForbidden

class TipsView(ListView):
    template_name="tips.html"
    
    def get_queryset():
        return super(Tipsview, self).get_queryset()
