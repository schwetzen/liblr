# Generated by Django 2.1.3 on 2018-11-19 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181118_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readingtip',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='readingtip',
            name='url',
            field=models.CharField(blank=True, max_length=20, verbose_name='URL'),
        ),
    ]
