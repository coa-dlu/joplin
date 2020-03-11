# Generated by Django 2.2.10 on 2020-03-11 15:58

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuidePage',
            fields=[
                ('janisbasepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base_page.JanisBasePage')),
                ('description', models.TextField(blank=True, verbose_name='Write a description of the guide')),
                ('description_ar', models.TextField(blank=True, null=True, verbose_name='Write a description of the guide')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Write a description of the guide')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Write a description of the guide')),
                ('description_vi', models.TextField(blank=True, null=True, verbose_name='Write a description of the guide')),
                ('sections', wagtail.core.fields.StreamField([('section', wagtail.core.blocks.StructBlock([('section_heading_en', wagtail.core.blocks.TextBlock(label='Heading [en]')), ('section_heading_es', wagtail.core.blocks.TextBlock(label='Heading [es]', required=False)), ('section_heading_ar', wagtail.core.blocks.TextBlock(label='Heading [ar]', required=False)), ('section_heading_vi', wagtail.core.blocks.TextBlock(label='Heading [vi]', required=False)), ('pages', wagtail.core.blocks.ListBlock(wagtail.core.blocks.PageChooserBlock(label='Page', page_type=['information_page.InformationPage', 'service_page.ServicePage']), help_text='Select existing pages in the order you want them                         to display within each heading.                        Pages should be added only once to any single guide.'))], label='Section'))], blank=True, verbose_name='Add a section header and pages to each section')),
            ],
            options={
                'abstract': False,
            },
            bases=('base_page.janisbasepage',),
        ),
        migrations.CreateModel(
            name='GuidePageContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GuidePageTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='guide_page.GuidePage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
