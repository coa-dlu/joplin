# Generated by Django 2.2.9 on 2020-02-11 07:54

from django.db import migrations

def create_group_page_permissions(apps, schema_editor):
    # Get all the page models we have related_departments on
    page_models = [
        apps.get_model('base', 'FormContainer'),
        apps.get_model('base', 'GuidePage'),
        apps.get_model('base', 'InformationPage'),
        apps.get_model('base', 'OfficialDocumentPage'),
        apps.get_model('base', 'ServicePage'),
        apps.get_model('events', 'EventPage'),
    ]

    # Get the group page permission model from wagtail
    GroupPagePermission = apps.get_model('wagtailcore', 'GroupPagePermission')

    # Find all the related departments on pages and create a wagtail
    # group page permissions object to connect the department (group) to the page
    for page_model in page_models:
        for page in page_model.objects.all():
            if page.related_departments:
                for page_related_department in page.related_departments.all():
                    GroupPagePermission.objects.create(
                        group=page_related_department.related_department.department,
                        page=page,
                        permission_type='edit'
                    )


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200211_0648'),
    ]

    operations = [
        migrations.RunPython(create_group_page_permissions),
    ]

