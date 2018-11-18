from django.db import models


class ReadingTip(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30)
    url = models.CharField(verbose_name="URL", max_length=20)
    description = models.CharField(verbose_name="Description", max_length=50)
