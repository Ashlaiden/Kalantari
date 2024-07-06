# myapp/templatetags/custom_filters.py
from django import template


register = template.Library()


@register.filter
def multiply(value, arg):
    return value * arg


@register.filter
def tax(value, arg):
    return ((value * arg) / 100) * 9


@register.filter
def final_after_tax(value, arg):
    return (value * arg) + (((value * arg) / 100) * 9)


@register.filter
def format_number(value):
    try:
        value = int(value)
        return f"{value:,}"
    except (ValueError, TypeError):
        return value

