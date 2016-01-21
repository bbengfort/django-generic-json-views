# tests.views_tests
# Test the Generic views in the json_views library
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Feb 12 11:36:47 2015 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: views_tests.py [] benjamin@bengfort.com $

"""
Test the Generic views in the json_views library
"""

##########################################################################
## Imports
##########################################################################

import os
import sys
import codecs
import datetime
import unittest

from json_views.views import *

from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory


##########################################################################
## Fixtures
##########################################################################

data = {
    'number': 42,
    'name': 'Sonny Bono',
    'email': 'john.doe@example.com',
    'birthday': datetime.date(1990, 10, 31),
    'registered': datetime.datetime(2006, 4, 8, 12, 43, 12),
    'balance': 235.03,
    'isadmin': False,
    'groceries': [
        'apples',
        'bananas',
        'pears',
    ],
    'nested': {
        'complex': True,
        'value': 2153.23412
    }
}

FIXTURES  = os.path.join(os.path.dirname(__file__), "fixtures")
PYVERSION = sys.version_info[0]

def read_fixture(name, version=PYVERSION, fixtures=FIXTURES):
    """
    Reads data from a fixture with the correct Python version
    """
    name, ext = os.path.splitext(name)
    name = "{}-py{}{}".format(name, version, ext)
    path = os.path.join(fixtures, name)

    with codecs.open(path, 'r', 'utf-8') as f:
        return f.read()


class BasicView(JSONDataView):

    def get_context_data(self, **kwargs):
        context = kwargs
        context.update(data)
        return context

##########################################################################
## Test Cases
##########################################################################

class JSONSerializationTests(TestCase):

    def test_dumps(self):
        """
        Assert that dumps can serialize JSON
        """
        self.assertEqual(len(dumps(data)), len(read_fixture('data.json')))

    def test_dumps_opts(self):
        """
        Assert that the dumps function passes kwargs
        """
        self.assertEqual(dumps(data, indent=2, sort_keys=True), read_fixture('pretty-data.json'))

    @unittest.skip("pending implementation")
    def test_dumps_models(self):
        """
        Test that the LazyJSONEncoder serializes models
        """
        pass

    @unittest.skip("pending implementation")
    def test_dumps_queryset(self):
        """
        Test that the LazyJSONEncoder serializes querysets
        """
        pass

    @unittest.skip("pending implementation")
    def test_dumps_model_serialize(self):
        """
        Test that the LazyJSONEncoder serializes models with a serialize method
        """
        pass

class JSONDataViewTests(TestCase):

    def setUp(self):
        self.view = BasicView.as_view()
        self.factory = RequestFactory()

    def test_400_error(self):
        """
        Test a 405 error on post
        """
        request  = self.factory.post('/', 'f00bar', content_type='application/json')
        response = self.view(request)
        self.assertEqual(response.status_code, 405)

    def test_200_get(self):
        """
        Test a 200 response on get
        """
        request  = self.factory.get('/', content_type='application/json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_json_response_get(self):
        """
        Assert a JSONResponse is returned
        """
        request  = self.factory.get('/', content_type='application/json')
        response = self.view(request)
        self.assertTrue(isinstance(response, JSONResponse))

    @unittest.skip("pending implementation")
    def test_remove_duplicate_obj(self):
        """
        Test that duplicate objects are removed
        """
        pass

    @unittest.skip("pending implementation")
    def test_render_to_response(self):
        """
        Test HTTP rendering of the response
        """
        pass

class JSONDetailViewTests(TestCase):
    pass

class JSONListViewTests(TestCase):
    pass

class JSONPaginationTests(TestCase):
    pass

class JSONFormViewTests(TestCase):
    pass
