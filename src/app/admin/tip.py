from django.contrib import admin


class ReadingTipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content_type', 'title', 'description',)
    ordering = ('-id',)
    search_fields = ('title', 'url', 'description',)
