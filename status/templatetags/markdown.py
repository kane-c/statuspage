from __future__ import unicode_literals

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
import markdown2


register = template.Library()


@register.filter
@stringfilter
def markdown(value):
    return mark_safe(markdown2.markdown(value, safe_mode=True))
