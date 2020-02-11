# Generated by Django 2.2.9 on 2020-02-11 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200211_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidepagerelateddepartments',
            name='page',
        ),
        migrations.RemoveField(
            model_name='guidepagerelateddepartments',
            name='related_department',
        ),
        migrations.RemoveField(
            model_name='informationpagerelateddepartments',
            name='page',
        ),
        migrations.RemoveField(
            model_name='informationpagerelateddepartments',
            name='related_department',
        ),
        migrations.RemoveField(
            model_name='officialdocumentpagerelateddepartments',
            name='page',
        ),
        migrations.RemoveField(
            model_name='officialdocumentpagerelateddepartments',
            name='related_department',
        ),
        migrations.RemoveField(
            model_name='servicepagerelateddepartments',
            name='page',
        ),
        migrations.RemoveField(
            model_name='servicepagerelateddepartments',
            name='related_department',
        ),
        migrations.DeleteModel(
            name='FormContainerRelatedDepartments',
        ),
        migrations.DeleteModel(
            name='GuidePageRelatedDepartments',
        ),
        migrations.DeleteModel(
            name='InformationPageRelatedDepartments',
        ),
        migrations.DeleteModel(
            name='OfficialDocumentPageRelatedDepartments',
        ),
        migrations.DeleteModel(
            name='ServicePageRelatedDepartments',
        ),
    ]
