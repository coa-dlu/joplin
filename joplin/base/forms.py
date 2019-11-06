from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.core.models import Page, PageRevision
from django.core.exceptions import ValidationError

# copying Sergio's magic code


def get_http_request():
    """
        Probably a bad-practice & non-performant approach,
        returns a django request object.
        https://docs.djangoproject.com/en/2.2/ref/request-response/
    """
    import inspect
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            # looking good...
            return frame_record[0].f_locals['request']
            break
    else:
        # looking bad...
        return None


class ServicePageForm(WagtailAdminPageForm):
    def clean(self):
        """
        ways to limit scope:
        changed fields,
        then exclude fields that are required

        self.changed_data = list of fields changed

        self[field_name].data or as_text (might be useful for streamfields)
        looks like this is working, atm tho it just wont let you publish any empty fields :-D
        """
        def check_for_empties(form_entries):
            entries = []
            # alt: self.fields[entry]
            for entry in form_entries:
                # TODO really only works for strings atm, super lazy hack to ignore streamfields and prevent render error
                if not self[entry].data and str(type(self.fields[entry])) == "<class 'django.forms.fields.CharField'>":
                    self.add_error(entry, "It's empty!")
                    entries.append(entry)
                    ValidationError(('Invalid value, empty'), code='invalid')
            return entries
        cleaned_data = super().clean()
        # hacky way  to check if its publish vs draft, using the hacky function above
        request = get_http_request()
        is_publishing = bool(request.POST.get('action-publish'))

        if is_publishing:
            changed_fields = self.changed_data
            check_changed = check_for_empties(changed_fields)
            keys = list(self.fields.keys())
            if not check_changed:
                check_all = check_for_empties(keys)
        return cleaned_data


class ProcessPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class InformationPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DepartmentPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TopicPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TopicCollectionPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class OfficialDocumentPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class GuidePageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class FormPageForm(WagtailAdminPageForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
