# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
from pages.base_page.models import


def add_pageviewpermissions(apps, schema_editor):
    # Get model
    JanisBasePage = apps.get_model('base_page.JanisBasePage') #todo: check this
    PageViewRestriction = apps.get_model('wagtailcore.PageViewRestriction')

    all_pages = JanisBasePage.objects.all()

    # https://blog.etianen.com/blog/2013/06/08/django-querysets/
    for page in all_pages.iterator():
        pvr = PageViewRestriction.objects.create(
            page=page,
            restriction_type=PageViewRestriction.GROUPS,
        )
        for group_permission in page.group_permissions.all():
            if (group_permission and
                group_permission.group and
                group_permission.group.department):
                   # and group_permission.group.department.department_page): #actually do we need the page here?
                pvr.groups.set(group_permission.group.department)


class Migration(migrations.Migration):

    dependencies = [
        ('base_page', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_pageviewpermissions()),
    ]
