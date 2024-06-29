# myapp/templatetags/custom_filters.py
from django import template


register = template.Library()


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def format_number(value):
    try:
        value = int(value)
        return f"{value:,}"
    except (ValueError, TypeError):
        return value

