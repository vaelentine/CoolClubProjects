from django import template
register = template.Library()


@register.filter
def class_name(value):
    return value.__class__.__name__


@register.filter
def field_names(value):
    return value._meta.fields


@register.filter
def lookup(value, key):
    return value[key]