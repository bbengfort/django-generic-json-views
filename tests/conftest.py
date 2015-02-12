# tests.conftest
# Configure Django for testing
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Feb 12 11:52:30 2015 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: conftests.py [] benjamin@bengfort.com $

"""
Configure Django for testing. Copied and modified from the Django Rest
Framework conftest.py file for use in testing this app:

https://github.com/tomchristie/django-rest-framework/blob/master/tests/conftest.py
"""

def pytest_configure():
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        DATABASES={'default': {'ENGINE': 'django.db.backends.sqlite3',
                               'NAME': ':memory:'}},
        SITE_ID=1,
        SECRET_KEY='not very secret in tests',
        USE_I18N=True,
        USE_L10N=True,
        STATIC_URL='/static/',
        ROOT_URLCONF='tests.urls',
        TEMPLATE_LOADERS=(
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ),
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        )
    )

    try:
        import django
        django.setup()
    except AttributeError:
        pass
