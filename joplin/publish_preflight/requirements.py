from django.core.exceptions import ValidationError


# Check if field value is not empty
# Default criteria for FieldPublishRequirement
def is_not_empty(field_value):
    if isinstance(field_value, str):
        return not (not field_value.strip())
    else:
        return not (not field_value)


# Check if relation has at least one entry
# Default criteria for RelationPublishRequirement
def has_at_least_one(relation_value):
    return len(relation_value) > 0


def streamfield_has_length(stream_value):
    if not stream_value:
        return False
    return len(stream_value) > 0


placeholder_message = "Publish Requirement not met"


class PublishRequirementError(ValidationError):
    def __init__(self, *args, **kwargs):
        self.publish_error_data = kwargs.pop("publish_error_data", None)
        super(PublishRequirementError, self).__init__(*args, **kwargs)


class BasePublishRequirement:
    def evaluate(self, field_name, field_value):
        result = self.criteria(field_value)
        if not result:
            publish_requirement_error = PublishRequirementError(self.message, publish_error_data={
                "field_name": field_name,
                "message": self.message,
                "field_type": self.field_type,
            })
            return {
                "passed": False,
                "publish_requirement_error": publish_requirement_error,
            }
        else:
            return {
                "passed": True,
            }


# A Publish Requirement for a simple field
class FieldPublishRequirement(BasePublishRequirement):
    def __init__(self, field_name, criteria=is_not_empty, message=placeholder_message, langs=None):
        self.field_type = "field"
        self.field_name = field_name
        self.criteria = criteria
        self.message = message
        self.langs = langs

    def check_criteria(self, form):
        field_name = self.field_name
        data = form.cleaned_data
        # If field is not translated, then get check value of "field_name"
        if self.langs:
            for lang in self.langs:
                translated_field_name = f'{self.field_name}_{lang}'
                if translated_field_name in data:
                    field_value = data.get(translated_field_name)
                    return self.evaluate(translated_field_name, field_value)
                else:
                    raise KeyError(f"Field required for publish '{translated_field_name}' does not exist.")
        else:
            field_value = data.get(field_name)
            return self.evaluate(field_name, field_value)


# A Publish Requirement for a related ClusterableModel
class RelationPublishRequirement(BasePublishRequirement):
    def __init__(self, field_name, criteria=has_at_least_one, message=placeholder_message):
        self.field_type = "relation"
        self.field_name = field_name
        self.criteria = criteria
        self.message = message

    def check_criteria(self, form):
        field_name = self.field_name
        formsets = form.formsets
        if field_name in formsets:
            data = formsets.get(field_name).cleaned_data
            return self.evaluate(field_name, data)
        else:
            raise KeyError(f"Field required for publish '{field_name}' does not exist.")


class ConditionalPublishRequirement:
    def __init__(self, requirement1, operation, requirement2, message=placeholder_message):
        self.requirement1 = requirement1
        self.operation = operation
        self.requirement2 = requirement2
        self.message = message

    operation_map = {
        "or": lambda a, b: a or b,
        "and": lambda a, b: a and b,
    }

    # TODO: finish
    def check_criteria(self, value):
        op_func = self.operation_map[self.operation]
        return op_func(
            self.requirement1.check_criteria(value),
            self.requirement2.check_criteria(value),
        )


class StreamFieldPublishRequirement(BasePublishRequirement):
    """Publishing Requirement for Streamfields"""
    def __init__(self, field_name, criteria=streamfield_has_length, message=placeholder_message, langs=None,
                 streamfield_id=".stream-field"):
        self.field_type = "streamfield"
        self.field_name = field_name
        self.criteria = criteria
        self.message = message
        self.langs = langs
        self.streamfield_id = streamfield_id

    def evaluate_streamfield(self, field_name, field_value, streamfield_id):
        """
        :param field_name: name of required field
        :param field_value: value of required field
        :param streamfield_id: selector passed to PublishRequirementError for publishing the error
        :return: dictionary with "passed", a boolean of the result of checking the field_value against the criteria.
        If false, a PublishRequirementError is included
        """
        result = self.criteria(field_value)
        if not result:
            publish_requirement_error = PublishRequirementError(self.message, publish_error_data={
                "field_name": field_name,
                "message": self.message,
                "field_type": self.field_type,
                "streamfield_id": streamfield_id
            })
            return {
                "passed": False,
                "publish_requirement_error": publish_requirement_error,
            }
        else:
            return {
                "passed": True,
            }

    def check_criteria(self, form):
        """
        Goes through form looking for the field_name, appending the appropriate language tag to end of field_name
        if self.langs. Calls self.evaluate_streamfield if field_name exists, otherwise returns a PublishRequirementError

        If the streamfield is missing elements, the form does not include it in cleaned_data.

        :param form: form being checked
        :return: result of self.evaluate_streamfield
        """
        field_name = self.field_name
        streamfield_id = self.streamfield_id
        data = form.cleaned_data
        # If field is translated, then check value of each applicable language
        if self.langs:
            for lang in self.langs:
                translated_field_name = f'{self.field_name}_{lang}'
                if translated_field_name in data:
                    field_value = data.get(translated_field_name)
                    return self.evaluate_streamfield(translated_field_name, field_value, streamfield_id)
                else:
                    # if the section doesnt have a header and a page attached, the section isn't added to the
                    # cleaned_data at all
                    publish_requirement_error = PublishRequirementError(self.message, publish_error_data={
                        "field_name": field_name,
                        "message": self.message,
                        "field_type": self.field_type,
                        "streamfield_id": self.streamfield_id,
                    })
                    return {
                        "passed": False,
                        "publish_requirement_error": publish_requirement_error,
                    }
                    # raise KeyError(f"Field required for publish '{translated_field_name}' does not exist.")
        else:
            # If field is not translated, then get check value of "field_name"
            field_value = data.get(field_name)
            return self.evaluate_streamfield(field_name, field_value, streamfield_id)


# sample
publish_requirements = (
    FieldPublishRequirement("description", langs=["en"]),
    FieldPublishRequirement("additional_content", langs=["en"]),
    ConditionalPublishRequirement(
        RelationPublishRequirement("topic"),
        "or",
        ConditionalPublishRequirement(
            RelationPublishRequirement("related_department"),
            "or",
            FieldPublishRequirement("coa_global"),
        ),
        message="You must have at least 1 topic or 1 department or 'Top Level' checked."
    ),
)
