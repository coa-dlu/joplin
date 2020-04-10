# Generated by Django 2.2.12 on 2020-04-10 10:54

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('department_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('department_page', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='department_page.DepartmentPage')),
            ],
            options={
                'verbose_name_plural': 'Departments',
                'ordering': ['name'],
            },
            bases=('auth.group', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
    ]
