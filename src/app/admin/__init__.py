from django.contrib import admin
from app.models import *
from app.admin.tip import ReadingTipAdmin
from app.admin.user import UserAdmin


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ReadingTip, ReadingTipAdmin)
