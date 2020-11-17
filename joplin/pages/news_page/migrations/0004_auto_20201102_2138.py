# Generated by Django 2.2.16 on 2020-11-02 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_page', '0003_auto_20201002_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspage',
            name='written_for_department',
            field=models.ForeignKey(blank=True, help_text="If this news is written for another department, select that department below. This ensures that this news is associated with that department's news content", null=True, on_delete=django.db.models.deletion.SET_NULL, to='department_page.DepartmentPage', verbose_name='Assign a different department'),
        ),
    ]
