from django.contrib.auth import mixins
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.db.models import Q

from app.models import ReadingTip


class CalendarView(mixins.LoginRequiredMixin, generic.TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'calendar.html'


class EventView(mixins.LoginRequiredMixin, generic.View):
    login_url = reverse_lazy('login')

    def get(self, request):
        start = request.GET.get('start', None)
        end = request.GET.get('end', None)

        q = (Q(start_date__gte=start) | Q(end_date__gte=start)) & (Q(start_date__lte=end) | Q(end_date__lte=end))

        tips = ReadingTip.objects.filter(q, user=request.user, is_deleted=False)

        def mapping(tip):
            return dict(
                title=tip.title,
                start=tip.start_date,
                end=tip.end_date,
                url=reverse('tip', kwargs={'tip_id': tip.id})
            )

        events = list(map(mapping, tips))

        return JsonResponse(events, safe=False)
