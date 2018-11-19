from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_superuser', 'is_staff', 'is_active',)
    list_filter = ('is_superuser', 'is_staff', 'is_active',)
    ordering = ('-id',)
