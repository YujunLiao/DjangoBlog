"""
================================================================================
* File name:
* Author:LYJ
* Description: Django settings for mBlog project.
Generated by 'django-admin startproject' using Django 2.1.1.
For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
--------------------------------------------------------------------------------
* Attention:
================================================================================
* Modifier:LYJ
* Modification time: 2019-04-13
* Modify content:
+ Modify the code according to the google code style.
--------------------------------------------------------------------------------
+ Debug option: When it is set to TRUE, this application will in DEBug mode, then
if a bug is triggered , it showes the bug directly on the web browser. On the contrary,
if it is set to False, it show a 502,503 page, then you have to look up the bug in log file.
--------------------------------------------------------------------------------
+ INSTALLED_APPS: add apps 'markdown_deux' , 'mainsite' and 'django.contrib.sitemaps'here.
'mainsite' is the app for the website, add it to take effect. 'markdown_deux' is to support
the usage of Markdown. 'django.contrib.sitemaps' is to support the function of showing site map .
--------------------------------------------------------------------------------
+ TEMPLATES: Add the key-value pair " 'DIRS': [os.path.join(BASE_DIR, 'templates')] " then
the method "get_template" ,can search html template files under the path "BASE_DIR/templates",
to be more precise, the BASE_DIR is the absolute path of this project, for example, now
the BASE_DIR should be /var/www/mBlog/mBlog, so the templates path is /var/www/mBlog/mBlog/templates.
--------------------------------------------------------------------------------
+ TIME_ZONE: Change the time zone to 'Asia/Shanghai'.
--------------------------------------------------------------------------------
+ STATIC_URL:
--------------------------------------------------------------------------------
+ STATIC_ROOT: Set a static root file. run the command '  ' to collect all the static source
into this file. This file is work for the web server, when the browser request for static source,
return them through web server, such as nginx, instead of django.
--------------------------------------------------------------------------------
+ STATICFILES_DIRS: Add a file that created for storing the common static resources used
by several differnt applications into the search scope , which means that when some static
source is requested, it will search not only the path under all the app, but also the file
added in STATICFILES_DIRS.
================================================================================
"""


import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y30l@t19w%4_y3c=dk_xe)m#zqr0$nt^t82##4c!ggk+3#mlf_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdown_deux',
    'mainsite',
    'django.contrib.sitemaps',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mBlog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mBlog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "mainsite"),
]
