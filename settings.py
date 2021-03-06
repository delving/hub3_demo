# -*- coding: utf-8 -*-
"""Common settings and globals."""

from os.path import abspath, dirname, sep

from django.utils.translation import ugettext_lazy as _

from kombu import Queue, Exchange

from django.utils.translation import ugettext_lazy as _

# Get the Site name first:
SITE_NAME = dirname(abspath(__file__)).split(sep)[-1]

print(("Starting with settings from {}".format(SITE_NAME)))
##################
# BASE SETTINGS #
##################

# Allow settings to be shared between all nave projects to be loaded first.
# The remainder of this settings file contains project specific settings
try:
    from nave.base_settings import *
except ImportError:
    print("Unable to load the base_settings.py. Please make sure the base_settings.py is on your "
          "sys path")
    raise

##################
# BASE OVERRIDES #
##################


########################
# MAIN DJANGO SETTINGS #
########################


########## PATH CONFIGURATION

# Name of the directory for the project.
PROJECT_DIRNAME = SITE_NAME

PROJECT_ROOT = dirname(abspath(__file__))

########## END PATH CONFIGURATION

########## END GENERAL CONFIGURATION

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('en', _('English')),
)

USE_I18N = True

USE_L10N = False

SOLID_I18N_USE_REDIRECTS = False

SOLID_I18N_HANDLE_DEFAULT_PREFIX = True

SOLID_I18N_DEFAULT_PREFIX_REDIRECT = True

ROSETTA_MESSAGES_PER_PAGE = 100

ROSETTA_AUTO_COMPILE = True

########## SITE CONFIGURATION
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost",
                 "acc.{}.delving.org".format(SITE_NAME),
                 "prod.{}.delving.eu".format(SITE_NAME),
                 "{}.hub3.delving.org".format(SITE_NAME),
                 "{}.localhost".format(SITE_NAME)]

########## END SITE CONFIGURATION

########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
# FIXTURE_DIRS = (
#     normpath(join(PROJECT_ROOT, 'fixtures')),
# )
########## END FIXTURE CONFIGURATION


########## MIDDLEWARE CONFIGURATION

# Every cache key will get prefixed with this value - here we set it to
# the name of the directory the project is in to try and use something
# project specific.
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME

########## END MIDDLEWARE CONFIGURATION


################
# APPLICATIONS #
################

########## APP CONFIGURATION


# Apps specific for this project go here.
PROJECT_APPS = (
    "nave.projects.demo",
    "nave.diw",
)


# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = PROJECT_APPS + INSTALLED_APPS
########## END APP CONFIGURATION

USE_WAGTAIL_CMS = False

##########################
# RDF store configuration #
##########################

RDF_STORE_PORT = 3030  # Port for triple store HTTP server

RDF_STORE_HOST = "http://localhost"

RDF_BASE_URL = "demo.hub3.delving.org"

RDF_STORE_DB = SITE_NAME

RDF_ROUTED_ENTRY_POINTS =   ["acc.{}.delving.org".format(SITE_NAME),
                            "prod.{}.delving.eu".format(SITE_NAME),
                            "{}.localhost:8000".format(SITE_NAME),
                            "{}.hub3.delving.org".format(SITE_NAME)]

RDF_STORE_TRIPLES = False

###################
# Elastic search  #
###################

ES_URLS = ['localhost:9200']

ES_DISABLED = False  # useful for debugging

ES_TIMEOUT = 5

ES_ROWS = 20

#########################
# DataSet configuration #
#########################

BULK_API_ASYNC = True

NARTHEX_URL = "http://{}.localhost/narthex".format(SITE_NAME)
NARTHEX_API_KEY = "secret"

SCHEMA_REPOSITORY = "http://schemas.delving.eu/"
DEFAULT_INDEX_SCHEMA = "icn"
ENABLED_SCHEMAS = ['abm', 'icn', 'tib']
ORG_ID = "demo"
ZIPPED_SEARCH_RESULTS_DOWNLOAD_FOLDER = "/tmp"

#############################
## Celery Broker settings.  #
#############################

# queues and routes
CELERY_DEFAULT_QUEUE = SITE_NAME
CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_DEFAULT_ROUTING_KEY = SITE_NAME

RECORD_QUEUE = "{}_records".format(SITE_NAME)
mapping_queue = "{}_mapping".format(SITE_NAME)
big_download_queue = "{}_download".format(SITE_NAME)
webresource_queue = "{}_webresource".format(SITE_NAME)

CELERY_QUEUES = (
    Queue(SITE_NAME, Exchange(SITE_NAME), routing_key=SITE_NAME),
    Queue(RECORD_QUEUE, Exchange(RECORD_QUEUE), routing_key=RECORD_QUEUE),
    Queue(mapping_queue, Exchange(mapping_queue), routing_key=mapping_queue),
    Queue(big_download_queue, Exchange(big_download_queue), routing_key=big_download_queue),
    Queue(webresource_queue, Exchange(webresource_queue), routing_key=webresource_queue),
)


###################
# DEPLOY SETTINGS #
###################

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key should only be used for development and testing.
SECRET_KEY = "l#5lyn$-z@ygw$uj-*+4%%rmz5j25btvud5v_^p3(5x$-p1_(k"
NEVERCACHE_KEY = "uj$_u7wg34ufb3zdv_*bcd@2s+e43eu^+!890vf$m*)gw8rg13"
########## END SECRET CONFIGURATION


####################################
#    Django Suit Configuration     #
####################################

# Django Suit configuration example
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'Hub3 Login',
    # 'HEADER_DATE_FORMAT': 'l, j. F Y',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    # 'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    'LIST_PER_PAGE': 15
}

##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from nave.projects.demo.local_settings import *
except ImportError:
    print("Unable to load the local_settings.py. Please create one from local_settings.py.template.")
    raise
