# Generated by Django 2.0.8 on 2018-09-27 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_auto_20180927_0500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicepagestep',
            name='page',
        ),
        migrations.DeleteModel(
            name='ServicePageStep',
        ),
    ]
