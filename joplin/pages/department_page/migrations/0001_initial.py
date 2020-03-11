# Generated by Django 2.2.10 on 2020-03-11 15:58

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_page', '0001_initial'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentPage',
            fields=[
                ('janisbasepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_page.JanisBasePage')),
                ('what_we_do', wagtail.core.fields.RichTextField(blank=True, verbose_name='What we do')),
                ('what_we_do_ar', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='What we do')),
                ('what_we_do_en', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='What we do')),
                ('what_we_do_es', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='What we do')),
                ('what_we_do_vi', wagtail.core.fields.RichTextField(blank=True, null=True, verbose_name='What we do')),
                ('mission', models.TextField(blank=True, verbose_name='Mission')),
                ('mission_ar', models.TextField(blank=True, null=True, verbose_name='Mission')),
                ('mission_en', models.TextField(blank=True, null=True, verbose_name='Mission')),
                ('mission_es', models.TextField(blank=True, null=True, verbose_name='Mission')),
                ('mission_vi', models.TextField(blank=True, null=True, verbose_name='Mission')),
                ('job_listings', models.URLField(blank=True, help_text='Link to a page with job listings.', verbose_name='Job listings url')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.TranslatedImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('base_page.janisbasepage',),
        ),
        migrations.CreateModel(
            name='DepartmentPageTopPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('department', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_pages', to='department_page.DepartmentPage')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page', verbose_name='Select a page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentPageRelatedPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('department', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_pages', to='department_page.DepartmentPage')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page', verbose_name='Select a page')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentPageDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('title', models.CharField(default='Director', max_length=255)),
                ('title_ar', models.CharField(default='Director', max_length=255, null=True)),
                ('title_en', models.CharField(default='Director', max_length=255, null=True)),
                ('title_es', models.CharField(default='Director', max_length=255, null=True)),
                ('title_vi', models.CharField(default='Director', max_length=255, null=True)),
                ('about', models.TextField(blank=True)),
                ('about_ar', models.TextField(blank=True, null=True)),
                ('about_en', models.TextField(blank=True, null=True)),
                ('about_es', models.TextField(blank=True, null=True)),
                ('about_vi', models.TextField(blank=True, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_directors', to='department_page.DepartmentPage')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.TranslatedImage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DepartmentPageContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='base.Contact')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='department_page.DepartmentPage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
