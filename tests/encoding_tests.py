#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tests.encoding_tests
# Encoding test to deal with issue #11
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Wed Mar 11 09:32:12 2015 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: encoding_tests.py [] benjamin@bengfort.com $

"""
Encoding test to deal with issue #11
"""

##########################################################################
## Imports
##########################################################################

import unittest

from json_views.views import *
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

##########################################################################
## Fixtures
##########################################################################

class UTFEncodedJSONView(JSONDataView):

    def get_context_data(self, **kwargs):
        context = super(UTFEncodedJSONView, self).get_context_data(**kwargs)
        context['test'] = u"Привет"
        return context

##########################################################################
## Test Case
##########################################################################

class EncodingTests(TestCase):

    def setUp(self):
        self.view = UTFEncodedJSONView.as_view()
        self.factory = RequestFactory()

    def test_encoding(self):
        """
        Ensure that the response has the correct encoding
        """

        request  = self.factory.get('/', content_type='application/json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

        # Check the content type for the charset
        self.assertEqual(response['Content-Type'], 'application/json; charset=utf-8')
