# tests
# Testing package for the Django Generic JSON views library
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Feb 12 09:16:22 2015 -0500
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@bengfort.com $

"""
Testing package for the Django Generic JSON views library
"""

##########################################################################
## Imports
##########################################################################

import unittest

from .conftest import pytest_configure

##########################################################################
## Configure Testing Environment
##########################################################################

pytest_configure()

##########################################################################
## Initialization tests
##########################################################################

class InitializationTests(unittest.TestCase):

    def test_sanity(self):
        """
        Check that the world is sane and 2+2=4
        """
        self.assertEqual(2+2, 4)

    def test_import(self):
        """
        Assert that we can import our library for testing
        """
        try:
            import json_views
        except ImportError:
            self.fail("Could not import json_views library")

    def test_version(self):
        """
        Reminder to bump version
        """
        import json_views
        self.assertEqual(json_views.get_version(), "0.8")
