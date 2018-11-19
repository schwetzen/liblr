from django.db import models


class ReadingTip(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30)
    url = models.CharField(verbose_name="URL", max_length=20, blank=True)
    description = models.TextField(verbose_name="Description", blank=True)
