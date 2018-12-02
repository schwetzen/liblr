from django.views.generic import TemplateView

class AccountSettingsView(TemplateView):
    template_name = "settings.html"
