import time

from django import template

register = template.Library()


@register.filter
def iso8601(value):
    return time.strftime("%Y-%m-%dT%H:%M:%S", value.timetuple()[:9])
