from django.shortcuts import redirect
from django.views.generic import TemplateView


class AccountSettingsView(TemplateView):
    template_name = "settings.html"


class AccountDeleteView(TemplateView):
    template_name = "confirm_delete.html"
    
    def post(self, *args, **kwargs):
        user_to_delete = self.request.user
        user_to_delete.is_active = False
        user_to_delete.save()

        return redirect('logout')
