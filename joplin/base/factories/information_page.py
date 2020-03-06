import factory
import wagtail_factories
from django.utils.text import slugify
from base.models import *
from pages.topic_page.models import TopicPage
from pages.information_page.models import InformationPageTopic, InformationPageContact, InformationPage
from . import PageFactory
from pytest_factoryboy import register


class InformationPageTopicFactory(factory.django.DjangoModelFactory):
    page = factory.SubFactory('base.factories.information_page.InformationPageFactory')
    # TODO: make this factory, atm it chooses from existing topic pages
    topic = factory.Iterator(TopicPage.objects.all())

    class Meta:
        model = InformationPageTopic


class InformationPageContactFactory(factory.django.DjangoModelFactory):
    page = factory.SubFactory('base.factories.information_page.InformationPageFactory')
    # TODO: make this factory
    contact = factory.Iterator(Contact.objects.all())

    class Meta:
        model = InformationPageContact


class InformationPageFactory(PageFactory):
    description = factory.Faker('text')
    options = wagtail_factories.StreamFieldFactory(
        {'option': factory.Faker('text')}
    )
    additional_content = factory.Faker('text')

    class Meta:
        model = InformationPage

    @factory.post_generation
    def create_related_objects(self, create, extracted, **kwargs):
        if create:
            InformationPageTopicFactory.create_batch(2, page=self)
            InformationPageContactFactory.create_batch(2, page=self)
