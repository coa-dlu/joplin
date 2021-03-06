from django.core.management.base import BaseCommand, CommandError
import pages.topic_page.fixtures as topic_page_fixtures

'''
    Loads topic page fixtures into your joplin environment.

    Run with:
    pipenv run python joplin/manage.py load_test_topic_pages
'''
class Command(BaseCommand):
    help = "Loads test data for manual exploration of test topic pages"

    def handle(self, *args, **options):
        topic_page_fixtures.load_all()
