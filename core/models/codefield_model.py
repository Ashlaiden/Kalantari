from django import forms
from django.db import models
from django.utils.safestring import mark_safe
import json
import ast


# A custom widget that renders a Python or JSON value as a textarea
class CodeWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = ""
        # Create a textarea element with the value as the text
        html = f'<textarea name="{name}" id="{name}" rows="10" cols="80">{value}</textarea>'
        return mark_safe(html)


# A custom field that can handle a Python or JSON value
class CodeField(models.TextField):
    def formfield(self, **kwargs):
        # Use the custom widget for rendering the field
        kwargs['widget'] = CodeWidget
        return super().formfield(**kwargs)

    def from_db_value(self, value, expression, connection):
        # Convert the string value to a Python or JSON object
        if not value:
            return None
        try:
            return json.loads(value)  # try JSON first
        except (TypeError, ValueError):
            return ast.literal_eval(value)  # try Python next

    def get_prep_value(self, value):
        # Convert the Python or JSON object to a string value
        if not value:
            return None
        return json.dumps(value) # use JSON for serialization


# A model that has a code field
# class MyModel(models.Model):
#     name = models.CharField(max_length=100)
#     code = CodeField()
