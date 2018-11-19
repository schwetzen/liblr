from django.contrib import admin


class ReadingTipAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'description',)
    ordering = ('-id',)
    search_fields = ('title', 'url', 'description',)
