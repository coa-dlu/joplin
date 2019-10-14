# Generated by Django 2.2.6 on 2019-10-14 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0093_janisbranchsettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='janisbranchsettings',
            name='janis_branch',
        ),
        migrations.AddField(
            model_name='janisbranchsettings',
            name='preview_janis_branch',
            field=models.TextField(blank=True, help_text='Janis branch to preview pages', null=True),
        ),
        migrations.AddField(
            model_name='janisbranchsettings',
            name='publish_janis_branch',
            field=models.TextField(blank=True, help_text='Janis branch to publish pages', null=True),
        ),
    ]
