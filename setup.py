#!/usr/bin/env python
# setup
# Setup script for django-generic-json-views
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Feb 12 12:31:28 2015 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: setup.py [] benjamin@bengfort.com $

"""
Setup script for django-generic-json-views
"""

##########################################################################
## Imports
##########################################################################

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError:
    raise ImportError("Could not import \"setuptools\"."
                      "Please install the setuptools package.")

##########################################################################
## Package Information
##########################################################################

version  = __import__('json_views').__version__

## Discover the packages
packages = find_packages(where=".", exclude=("tests", "docs", "venv"))

## Load the requirements
requires = []
with open('requirements.txt', 'r') as reqfile:
    for line in reqfile:
        requires.append(line.strip())

## Define the classifiers
classifiers = (
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP',
)

## Define the keywords
keywords = ('django', 'json', 'views', 'generic', 'class library')

## Define the description
long_description = "These are simple generic class-based views for rendering JSON without the muss and fuss of Django Rest Framework or similar (although, if you're doing an API, then that library is far better than this one! Documentation can be found at Read the Docs: http://django-generic-json-views.readthedocs.org/en/latest/"

## Define the configuration
config = {
    "name": "django-generic-json-views",
    "version": version,
    "url": 'https://github.com/bbengfort/django-generic-json-views',
    "download_url": "https://github.com/bbengfort/django-generic-json-views/tarball/v0.6.2",
    "license": 'Apache',
    "description": 'Class based generic views that render JSON data.',
    "long_description": long_description,
    "author": 'Benjamin Bengfort',
    "author_email": 'benjamin@bengfort.com',
    "maintainer": 'Benjamin Bengfort',
    "maintainer_email": 'benjamin@bengfort.com',
    "packages": packages,
    "install_requires": requires,
    "classifiers": classifiers,
    "keywords": keywords,
    "zip_safe": True,
    "scripts": [],
}

##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)
