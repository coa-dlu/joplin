# Generated by Django 2.2.11 on 2020-04-06 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200326_1045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='hours_exceptions',
        ),
        migrations.DeleteModel(
            name='ContactDayAndDuration',
        ),
        migrations.DeleteModel(
            name='DayAndDuration',
        ),
    ]
