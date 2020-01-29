from django.core.exceptions import ValidationError


# Check if field value is not empty
# Default criteria for PublishRequirementField
def is_not_empty(field_value):
    if isinstance(field_value, str):
        return not (not field_value.strip())
    else:
        return not (not field_value)


# Check if relation has at least one entry
# Default criteria for PublishRequirementRelation
def has_at_least_one(relation_value):
    return len(relation_value) > 1


def streamfield_has_length(stream_value):
    """
    cant just be if it has length, b/c that allows it to only have a heading and pass
    so we should check if it has pages attached as well as a heading
    also for other types of streamfiles its something diffrent. maybe not pages, but steps. its a different criteria
    perhaps those should be defined in the model. that feels cleanest. and then passed through to the model.
    :param stream_value:
    :return:
    """
    return len(stream_value) > 0

# move into guide page and uncomment the criteria in the definition below
def streamfield_has_pages(stream_value):
    #check length of stream value
    stream_data = stream_value.stream_data
    # check that we have any data in the streamfield
    if stream_data:
        struct_value = stream_data[0][1]
        values_list = list(struct_value.values())
        if values_list[0] and values_list[-1]:
            return True
    return False


placeholder_message = "Publish Requirement not met"


# A Publish Requirement for a simple field
class PublishRequirementField:
    def __init__(self, field_name, criteria=has_at_least_one, message=placeholder_message, langs=["en"]):
        self.field_name = field_name
        self.criteria = criteria
        self.message = ValidationError(message)
        self.langs = langs

    def evaluate(self, field_name, field_value):
        result = self.criteria(field_value)
        return {
            "result": result,
            "field_name": field_name,
            "message": self.message
        }

    def check_criteria(self, data):
        field_name = self.field_name
        # If field is not translated, then get check value of "field_name"
        if field_name in data:
            field_value = data.get(field_name)
            return self.evaluate(field_name, field_value)
        # If field is translated, then check value of each applicable language
        else:
            for lang in self.langs:
                translated_field_name = f'{self.field_name}_{lang}'
                if translated_field_name in data:
                    field_value = data.get(translated_field_name)
                    return self.evaluate(translated_field_name, field_value)
                else:
                    raise ValidationError(f"Field required for publish '{translated_field_name}' does not exist.")


# A Publish Requirement for a related ClusterableModel
class PublishRequirementRelation:
    def __init__(self, field_name, criteria=has_at_least_one, message=placeholder_message):
        self.field_name = field_name
        self.criteria = criteria
        self.message = message

    def evaluate(self, field_name, data):
        result = self.criteria(data)
        return {
            "result": result,
            "field_name": field_name,
            "message": self.message
        }

    def check_criteria(self, form):
        try:
            # there doesnt seem to be formsets on it, come back to this
            formsets = form.formsets
        except AttributeError:
            print(dir(form))
        field_name = self.field_name
        if field_name in formsets:
            data = formsets.get(field_name).cleaned_data
            return self.evaluate(field_name, data)
        else:
            raise ValidationError(f"Field required for publish '{field_name}' does not exist.")


class PublishRequirementConditional:
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


class PublishRequirementStreamField:
    #    def __init__(self, field_name, criteria=streamfield_has_length, message=placeholder_message, langs=["en"]):
    def __init__(self, field_name, criteria=streamfield_has_pages, message=placeholder_message, langs=["en"]):
        self.field_name = field_name
        self.criteria = criteria
        # from wagtail.core.blocks.stream_block import StreamBlockValidationError
        self.message = ValidationError(message, params={"field": field_name})
        self.langs = langs

    def evaluate(self, field_name, field_value):
        result = self.criteria(field_value)
        print('streamfield result:', result)
        return {
            "result": result,
            "field_name": field_name,
            "message": self.message
        }

    def check_criteria(self, data):
        field_name = self.field_name
        # If field is not translated, then get check value of "field_name"
        if field_name in data:
            field_value = data.get(field_name)
            return self.evaluate(field_name, field_value)
        # If field is translated, then check value of each applicable language
        else:
            for lang in self.langs:
                translated_field_name = f'{self.field_name}_{lang}'
                if translated_field_name in data:
                    field_value = data.get(translated_field_name)
                    return self.evaluate(translated_field_name, field_value)
                else:
                    # if the section doesnt have a header and a page attached, the section isn't added to the
                    # cleaned_data at all
                    return {
                        "result": False,
                        "field_name": field_name,
                        "message": self.message
                    }
                    # raise ValidationError(f"Field required for publish '{translated_field_name}' does not exist.")


# sample
publish_requirements = (
    PublishRequirementField("description"),
    PublishRequirementField("additional_content"),
    PublishRequirementConditional(
        PublishRequirementRelation("topic"),
        "or",
        PublishRequirementConditional(
            PublishRequirementRelation("related_department"),
            "or",
            PublishRequirementField("coa_global"),
        ),
        "You must have at least 1 topic or 1 department or 'Top Level' checked."
    ),
)
