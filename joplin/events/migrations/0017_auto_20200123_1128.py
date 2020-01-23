# Generated by Django 2.2.9 on 2020-01-23 11:28

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_auto_20200123_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='location_blocks',
            field=wagtail.core.fields.StreamField([('city_location', wagtail.core.blocks.StructBlock([('location_page', wagtail.core.blocks.PageChooserBlock(classname='do-not-hide', label='Location', page_type=['locations.LocationPage'])), ('additional_details_en', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [en]', required=False)), ('additional_details_es', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [es]', required=False)), ('additional_details_ar', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [ar]', required=False)), ('additional_details_vi', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [vi]', required=False))])), ('remote_location', wagtail.core.blocks.StructBlock([('name_en', wagtail.core.blocks.TextBlock(label='Name of venue [en]')), ('name_es', wagtail.core.blocks.TextBlock(label='Name of venue [es]', required=False)), ('name_ar', wagtail.core.blocks.TextBlock(label='Name of venue [ar]', required=False)), ('name_vi', wagtail.core.blocks.TextBlock(label='Name of venue [vi]', required=False)), ('street', wagtail.core.blocks.TextBlock(label='Street', required=False)), ('unit', wagtail.core.blocks.TextBlock(label='Unit', required=False)), ('city', wagtail.core.blocks.TextBlock(label='City', required=False)), ('state', wagtail.core.blocks.TextBlock(label='State', required=False)), ('country', wagtail.core.blocks.TextBlock(label='Country', required=False)), ('zip', wagtail.core.blocks.TextBlock(label='ZIP', required=False)), ('additional_details_en', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [en]', required=False)), ('additional_details_es', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [es]', required=False)), ('additional_details_ar', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [ar]', required=False)), ('additional_details_vi', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [vi]', required=False))]))], blank=True, verbose_name='Add location of event'),
        ),
    ]
