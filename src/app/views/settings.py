from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.shortcuts import redirect

from app.models.user import User


class AccountSettingsView(TemplateView):
    template_name = "settings.html"

class AccountDeleteView(DeleteView):
    model = User
    template_name = "confirm_delete.html"
    
    def delete(self, request):
        user_to_delete = self.user

        user_to_delete.is_active = False
        user_to_delete.is_deleted = True
        
        user_to_delete.save()

        return redirect('logout')
