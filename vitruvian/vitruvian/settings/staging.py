from .base import *

DEBUG = True

ROOT_URLCONF = 'vitruvian.urls.development'

GS_LOCATION = os.getenv('GS_LOCATION', 'staging')
GS_AUTO_CREATE_ACL = os.getenv('GS_AUTO_CREATE_ACL', 'publicRead')
GS_DEFAULT_ACL = os.getenv('GS_DEFAULT_ACL', 'publicRead')
GS_CUSTOM_ENDPOINT = os.getenv('GS_CUSTOM_ENDPOINT', None)
