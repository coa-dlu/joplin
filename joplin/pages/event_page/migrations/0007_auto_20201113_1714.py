# Generated by Django 2.2.16 on 2020-11-13 17:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('event_page', '0006_auto_20201104_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='location_blocks',
            field=wagtail.core.fields.StreamField([('city_of_Austin_location', wagtail.core.blocks.StructBlock([('location_page', wagtail.core.blocks.PageChooserBlock(classname='do-not-hide', label='Location', page_type=['location_page.LocationPage'])), ('additional_details_en', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [en]', required=False)), ('additional_details_es', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [es]', required=False)), ('additional_details_ar', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [ar]', required=False)), ('additional_details_vi', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [vi]', required=False))])), ('remote_non_COA_location', wagtail.core.blocks.StructBlock([('name_en', wagtail.core.blocks.TextBlock(label='Name of venue [en]')), ('name_es', wagtail.core.blocks.TextBlock(label='Name of venue [es]', required=False)), ('name_ar', wagtail.core.blocks.TextBlock(label='Name of venue [ar]', required=False)), ('name_vi', wagtail.core.blocks.TextBlock(label='Name of venue [vi]', required=False)), ('street', wagtail.core.blocks.TextBlock(label='Street', required=False)), ('unit', wagtail.core.blocks.TextBlock(label='Unit', required=False)), ('city', wagtail.core.blocks.TextBlock(label='City', required=False)), ('state', wagtail.core.blocks.TextBlock(label='State', required=False)), ('zip', wagtail.core.blocks.TextBlock(label='ZIP', required=False)), ('additional_details_en', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [en]', required=False)), ('additional_details_es', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [es]', required=False)), ('additional_details_ar', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [ar]', required=False)), ('additional_details_vi', wagtail.core.blocks.TextBlock(label='Any other necessary location details, such as room number [vi]', required=False))])), ('virtual_event', wagtail.core.blocks.StructBlock([('event_link', wagtail.core.blocks.TextBlock(label='Event link or location')), ('additional_information_en', wagtail.core.blocks.TextBlock(label='Any other necessary information, such as meeting code [en]', required=False)), ('additional_information_es', wagtail.core.blocks.TextBlock(label='Any other necessary information, such as meeting code [es]', required=False)), ('additional_information_ar', wagtail.core.blocks.TextBlock(label='Any other necessary information, such as meeting code [ar]', required=False)), ('additional_information_vi', wagtail.core.blocks.TextBlock(label='Any other necessary information, such as meeting code [vi]', required=False))]))]),
        ),
    ]
