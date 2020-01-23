from django.db import models
from wagtail.core.blocks import StructBlock, PageChooserBlock, TextBlock
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    InlinePanel,
    FieldRowPanel,
    StreamFieldPanel,
)

from locations.models import LocationPage
from base.models import Contact
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from base.models import JanisBasePage
from base.models.widgets import countMe, countMeLongTextArea, AUTHOR_LIMITS
from modelcluster.models import ClusterableModel
from base.models.constants import DEFAULT_MAX_LENGTH, WYSIWYG_GENERAL
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class EventPage(JanisBasePage):
    janis_url_page_type = 'event'

    description = RichTextField(
        features=WYSIWYG_GENERAL,
        verbose_name='Full description of the event',
        blank=True
    )

    date = models.DateField(verbose_name="Event date", blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    location_blocks = StreamField(
        [
            ('city_location', StructBlock(
                [
                    ('location_page', PageChooserBlock(label="Location", page_type=[LocationPage], classname='do-not-hide')),
                    ('additional_details_en', TextBlock(label='Any other necessary location details, such as room number [en]', required=False)),
                    ('additional_details_es', TextBlock(label='Any other necessary location details, such as room number [es]', required=False)),
                    ('additional_details_ar', TextBlock(label='Any other necessary location details, such as room number [ar]', required=False)),
                    ('additional_details_vi', TextBlock(label='Any other necessary location details, such as room number [vi]', required=False)),
                ]
            )),
            ('remote_location', StructBlock(
                [
                    ('name_en', TextBlock(label='Name of venue [en]')),
                    ('name_es', TextBlock(label='Name of venue [es]', required=False)),
                    ('name_ar', TextBlock(label='Name of venue [ar]', required=False)),
                    ('name_vi', TextBlock(label='Name of venue [vi]', required=False)),
                    ('street', TextBlock(label='Street', required=False)),
                    ('unit', TextBlock(label='Unit', required=False)),
                    ('city', TextBlock(label='City', required=False)),
                    ('state', TextBlock(label='State', required=False)),
                    ('country', TextBlock(label='Country', required=False)),
                    ('zip', TextBlock(label='ZIP', required=False)),
                    ('additional_details_en', TextBlock(label='Any other necessary location details, such as room number [en]', required=False)),
                    ('additional_details_es', TextBlock(label='Any other necessary location details, such as room number [es]', required=False)),
                    ('additional_details_ar', TextBlock(label='Any other necessary location details, such as room number [ar]', required=False)),
                    ('additional_details_vi', TextBlock(label='Any other necessary location details, such as room number [vi]', required=False)),
                ],
                # label="Step With Options"
            )),
        ],
        verbose_name='Add location of event',
        # this gets called in the help panel
        # help_text='A step may have a basic text step or an options accordion which reveals two or more options',
        blank=True
    )

    event_is_free = models.BooleanField(verbose_name="This event is free", default=True)

    registration_url = models.URLField(
        verbose_name='The URL where the resident may register for the event, if needed',
        blank=True
    )

    contact = models.ForeignKey(Contact, related_name='+', blank=True, null=True, on_delete=models.SET_NULL)

    canceled = models.BooleanField(verbose_name="Cancel this event", default=False)

    content_panels = [
        FieldPanel('title_en', widget=countMe),
        FieldPanel('title_es', widget=countMe),
        FieldPanel('title_ar'),
        FieldPanel('title_vi'),
        # FieldPanel('description', widget=countMeLongTextArea),
        FieldPanel('description'),
        FieldPanel('date'),
        FieldRowPanel(
            children=[
                FieldPanel('start_time', classname='col3'),
                FieldPanel('end_time', classname='col3'),
            ],
            heading="Event time",
        ),
        StreamFieldPanel('location_blocks'),
        FieldPanel('event_is_free'),
        InlinePanel('fees', label='Fees'),
        FieldPanel('registration_url'),
        InlinePanel('related_departments', label='Related Departments'),
        SnippetChooserPanel('contact'),
        FieldPanel('canceled'),
    ]

    parent_page_types = ['base.HomePage']


class EventPageFee(ClusterableModel):
    page = ParentalKey(EventPage, related_name='fees', default=None)
    fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    fee_label = models.CharField(blank=True, verbose_name='Label (kids, adults, seniors, etc.)', max_length=DEFAULT_MAX_LENGTH)

    panels = [
        FieldRowPanel(
            children=[
                FieldPanel('fee', classname='col3'),
                FieldPanel('fee_label', classname='col9'),
            ],
        ),
    ]


class EventPageRelatedDepartments(ClusterableModel):
    page = ParentalKey(EventPage, related_name='related_departments', default=None)
    related_department = models.ForeignKey(
        "base.departmentPage",
        on_delete=models.PROTECT,
    )

    panels = [
        PageChooserPanel("related_department"),
    ]
