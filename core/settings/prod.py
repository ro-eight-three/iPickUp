from .base import *

DEBUG = False

# TODO
STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'built/minimized static-local'))

TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'site/templates-prod/'))

ALLOWED_HOSTS = [
    '*',
]
