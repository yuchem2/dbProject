from django import template

register = template.Library()


@register.filter
def id(value):
    return value._id


@register.filter
def index(value, idx):
    return value[idx]
