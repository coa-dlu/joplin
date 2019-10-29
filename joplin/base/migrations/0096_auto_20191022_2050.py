# Generated by Django 2.2.6 on 2019-10-22 20:50

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('base', '0095_merge_20191021_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guidepagetopic',
            name='toplink',
        ),
        migrations.RemoveField(
            model_name='informationpagetopic',
            name='toplink',
        ),
        migrations.RemoveField(
            model_name='officialdocumentpagetopic',
            name='toplink',
        ),
        migrations.RemoveField(
            model_name='servicepagetopic',
            name='toplink',
        ),
        migrations.AlterField(
            model_name='informationpage',
            name='options',
            field=wagtail.core.fields.StreamField([('option', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'link', 'ul', 'ol', 'code'], label='Option'))], blank=True, help_text='Options are needed when the reader needs to make a choice between a few options, such as ways to fill out a form (online, by phone, in person, etc.).', verbose_name='Add option sections as needed.'),
        ),
        migrations.AlterField(
            model_name='informationpage',
            name='options_ar',
            field=wagtail.core.fields.StreamField([('option', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'link', 'ul', 'ol', 'code'], label='Option'))], blank=True, help_text='Options are needed when the reader needs to make a choice between a few options, such as ways to fill out a form (online, by phone, in person, etc.).', null=True, verbose_name='Add option sections as needed.'),
        ),
        migrations.AlterField(
            model_name='informationpage',
            name='options_en',
            field=wagtail.core.fields.StreamField([('option', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'link', 'ul', 'ol', 'code'], label='Option'))], blank=True, help_text='Options are needed when the reader needs to make a choice between a few options, such as ways to fill out a form (online, by phone, in person, etc.).', null=True, verbose_name='Add option sections as needed.'),
        ),
        migrations.AlterField(
            model_name='informationpage',
            name='options_es',
            field=wagtail.core.fields.StreamField([('option', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'link', 'ul', 'ol', 'code'], label='Option'))], blank=True, help_text='Options are needed when the reader needs to make a choice between a few options, such as ways to fill out a form (online, by phone, in person, etc.).', null=True, verbose_name='Add option sections as needed.'),
        ),
        migrations.AlterField(
            model_name='informationpage',
            name='options_vi',
            field=wagtail.core.fields.StreamField([('option', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'link', 'ul', 'ol', 'code'], label='Option'))], blank=True, help_text='Options are needed when the reader needs to make a choice between a few options, such as ways to fill out a form (online, by phone, in person, etc.).', null=True, verbose_name='Add option sections as needed.'),
        ),
        migrations.CreateModel(
            name='TopicPageTopPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page', verbose_name='Select a page')),
                ('topic', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='top_pages', to='base.TopicPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
