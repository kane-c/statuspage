from __future__ import unicode_literals

from django.conf import settings


def settings_in_context(request):
    return {
        'brand_name': settings.BRAND_NAME,
        'GOOGLE_ANALYTICS_ID': settings.GOOGLE_ANALYTICS_ID,
    }
