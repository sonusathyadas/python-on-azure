import os
from envconfig import set_env_variables
import opencensus

set_env_variables()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@2$34)u+w=xy+v2n4a!q=dt836n&)6j@s4h$m^)5!u@86lmd!o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [  
    '*'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap4',
    'contactmanager',
    'storages'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'applicationinsights.django.ApplicationInsightsMiddleware',
    'opencensus.ext.django.middleware.OpencensusMiddleware'
]

APPLICATION_INSIGHTS = {
    # (required) Your Application Insights instrumentation key
    'ikey': os.environ.get('APP_INSIGHTS_iNSTRUMENTATION_KEY'),

    # (optional) By default, request names are logged as the request method
    # and relative path of the URL.  To log the fully-qualified view names
    # instead, set this to True.  Defaults to False.
    'use_view_name': True,

    # (optional) To log arguments passed into the views as custom properties,
    # set this to True.  Defaults to False.
    'record_view_arguments': True,

    # (optional) Exceptions are logged by default, to disable, set this to False.
    'log_exceptions': True,

    # (optional) Events are submitted to Application Insights asynchronously.
    # send_interval specifies how often the queue is checked for items to submit.
    # send_time specifies how long the sender waits for new input before recycling
    # the background thread.
    'send_interval': 1.0, # Check every second
    'send_time': 3.0, # Wait up to 3 seconds for an event

    # (optional, uncommon) If you must send to an endpoint other than the
    # default endpoint, specify it here:
    'endpoint': "https://dc.services.visualstudio.com/v2/track",
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # The application insights handler is here
        'appinsights': {
            'class': 'applicationinsights.django.LoggingHandler',
            'level': 'WARNING'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['appinsights'],
            'level': 'WARNING',
            'propagate': True,
        }
    }
}

OPENCENSUS = {
    'TRACE': {
        'SAMPLER': 'opencensus.trace.samplers.ProbabilitySampler(rate=1)',
        'EXPORTER': f'''opencensus.ext.azure.trace_exporter.AzureExporter(
            connection_string="InstrumentationKey={os.environ.get('APP_INSIGHTS_iNSTRUMENTATION_KEY')}"
        )'''
    }
}


ROOT_URLCONF = 'contactproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

WSGI_APPLICATION = 'contactproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USERNAME'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

AZURE_ACCOUNT_NAME=os.environ.get('STORAGE_ACCOUNT_NAME')
AZURE_STORAGE_KEY = os.environ.get('STORAGE_ACCOUNT_KEY')
AZURE_CUSTOM_DOMAIN = os.environ.get('STORAGE_ACCOUNT_DOMAIN')
AZURE_MEDIA_CONTAINER = os.environ.get('STORAGE_MEDIA_CONTAINER')
AZURE_STATIC_CONTAINER=os.environ.get('STORAGE_STATIC_CONTAINER')

if(DEBUG):
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_STATIC_CONTAINER}/'
    MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{AZURE_MEDIA_CONTAINER}/'
    STATICFILES_STORAGE = 'contactmanager.storage.azureblob.AzureStaticStorage'
    DEFAULT_FILE_STORAGE = 'contactmanager.storage.azureblob.AzureMediaStorage'
