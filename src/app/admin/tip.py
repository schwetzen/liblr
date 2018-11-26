from django.contrib import admin


class ReadingTipAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'content_type', 'title', 'description', 'has_been_read', 'is_deleted',)
    ordering = ('-id',)
    search_fields = ('title', 'url', 'description',)
