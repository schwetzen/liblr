from django.contrib.auth import mixins
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse_lazy


class CalendarView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'calendar.html'


class EventView(mixins.LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')

    def get(self, request):
        from django.db.models import Q

        start = request.GET.get('start', None)
        end = request.GET.get('end', None)

        objects = ...

        events = [
            {'title': 'lorem ipsum', 'start': '2018-12-03'},
            {'title': 'dolor sit amet', 'start': '2018-12-07'},
        ]

        return JsonResponse(events, safe=False)
