# Generated by Django 2.2.10 on 2020-03-11 15:58

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='JanisBasePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author_notes', wagtail.core.fields.RichTextField(blank=True, verbose_name='Notes for authors (Not visible on the resident facing site)')),
                ('coa_global', models.BooleanField(default=False, verbose_name='Make this a top level page')),
            ],
            options={
                'permissions': [('view_extra_panels', 'Can view extra panels'), ('view_snippets', 'Can view snippets'), ('add_snippets', 'Can add snippet'), ('delete_snippets', 'Can delete snippet')],
            },
            bases=('wagtailcore.page',),
        ),
    ]
