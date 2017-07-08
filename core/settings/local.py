from .base import *

DEBUG = True

STATICFILES_DIRS.append(os.path.join(BASE_DIR, 'site/static-local'))

TEMPLATES[0]['DIRS'].append(os.path.join(BASE_DIR, 'site/templates-local/'))

DISABLE_DEBUG_TOOLBAR = eval(os.environ["DISABLE_DEBUG_TOOLBAR"])

if not DISABLE_DEBUG_TOOLBAR:

    # for debug_toolbar to work IP address needs to be in these
    INTERNAL_IPS = [
        '127.0.0.1',
        '172.17.0.1',  # when run in docker container
    ]

    INSTALLED_APPS += [
        'debug_toolbar',
    ]

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE
