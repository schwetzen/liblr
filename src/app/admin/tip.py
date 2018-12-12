from django.contrib import admin


class ReadingTipAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'content_type', 'title', 'description',
        'start_date', 'end_date', 'has_been_read', 'is_deleted',
    )
    ordering = ('-id',)
    search_fields = ('title', 'url', 'description',)
