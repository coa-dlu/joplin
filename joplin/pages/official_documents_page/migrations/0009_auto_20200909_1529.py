# Generated by Django 2.2.15 on 2020-09-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official_documents_page', '0008_auto_20200811_2012'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='officialdocumentpage',
            index=models.Index(fields=['-date'], name='official_do_date_51dc9d_idx'),
        ),
    ]
