from .base import *

import sentry_sdk
from sentry_sdk import configure_scope
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = False

ROOT_URLCONF = 'vitruvian.urls.production'

GS_LOCATION = os.getenv('GS_LOCATION', '')
GS_AUTO_CREATE_ACL = os.getenv('GS_AUTO_CREATE_ACL', 'publicRead')
GS_DEFAULT_ACL = os.getenv('GS_DEFAULT_ACL', 'publicRead')
GS_CUSTOM_ENDPOINT = os.getenv('GS_CUSTOM_ENDPOINT', None)
