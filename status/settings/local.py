from __future__ import unicode_literals

from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',)\
                     + MIDDLEWARE_CLASSES\
                     + ('status.middleware.XForwardedForMiddleware',)

INSTALLED_APPS += ('debug_toolbar',)

INTERNAL_IPS = (
    '127.0.0.1',
)
