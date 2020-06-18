from pages.information_page.models import InformationPage
from pages.information_page.factories import InformationPageFactory
from pages.topic_page.models import TopicPage
from pages.topic_page.factories import TopicPageFactory
from pages.topic_collection_page.models import TopicCollectionPage
from pages.topic_collection_page.factories import TopicCollectionPageFactory
from pages.service_page.models import ServicePage
from pages.service_page.factories import ServicePageFactory
from pages.location_page.models import LocationPage
from pages.location_page.factories import LocationPageFactory
from pages.official_documents_page.models import OfficialDocumentPage
# from pages.official_documents_page.factories import OfficialDocumentPageFactory
from pages.department_page.models import DepartmentPage
from pages.department_page.factories import DepartmentPageFactory
from pages.event_page.models import EventPage
from pages.event_page.factories import EventPageFactory
from snippets.theme.models import Theme
from snippets.theme.factories import ThemeFactory
from pages.form_container.models import FormContainer
from pages.form_container.factories import FormContainerFactory
from pages.news_page.factories import NewsPage, NewsPageFactory


# TODO: Perhaps there is a better way to organize this all in one place.
page_type_map = {
    "information": {
        "model": InformationPage,
        "factory": InformationPageFactory,
    },
    "topic": {
        "model": TopicPage,
        "factory": TopicPageFactory,
    },
    "topics": {
        "model": TopicPage,
        "factory": TopicPageFactory,
    },
    "topiccollection": {
        "model": TopicCollectionPage,
        "factory": TopicCollectionPageFactory,
    },
    "services": {
        "model": ServicePage,
        "factory": ServicePageFactory,
    },
    "location": {
        "model": LocationPage,
        "factory": LocationPageFactory,
    },
    # "official_document": {
    #     "model": OfficialDocumentPage,
    #     "factory": OfficialDocumentPageFactory,
    # },
    "department": {
        "model": DepartmentPage,
        "factory": DepartmentPageFactory,
    },
    "event": {
        "model": EventPage,
        "factory": EventPageFactory,
    },
    "news": {
        "model": NewsPage,
        "factory": NewsPageFactory,
    },
    # Theme isn't an importer page_type, but we do create_fixtures for it.
    "theme": {
        "model": Theme,
        "factory": ThemeFactory,
    },
    "form": {
        "model": FormContainer,
        "factory": FormContainerFactory,
    }
}
