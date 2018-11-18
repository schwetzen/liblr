from django.db import models


class ReadingTip(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
