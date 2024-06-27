#!/usr/bin/python3
"""
This deefines unittests for Amenity class (models/amenity.py).
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
import datetime
from time import sleep
import os


class TestAmenity(unittest.TestCase):
    """Testing instantiation of Amenity class."""

    # Testing type
    def test_type(self):
        am = Amenity()
        self.assertEqual(Amenity, type(am))

    def test_type_public_attr(self):
        am = Amenity()
        self.assertEqual(str, type(am.name))

    def test_type_id(self):
        am = Amenity()
        self.assertEqual(str, type(am.id))

    def test_type_created_at(self):
        am = Amenity()
        self.assertEqual(datetime.datetime, type(am.created_at))

    def test_type_update_at(self):
        am = Amenity()
        self.assertEqual(datetime.datetime, type(am.updated_at))

    # Testing id
    def test_unique_id(self):
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        am1 = Amenity()
        sleep(0.02)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_consecutive_updated_at(self):
        am1 = Amenity()
        sleep(0.02)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        am = Amenity()
        am.name = "Holberton"
        am.email = "janesmith@gmail.com"
        self.assertTrue(hasattr(am, "name") and hasattr(am, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        am = Amenity()
        am_key = "Amenity." + am.id
        keys = storage.all().keys()
        self.assertTrue(am_key in keys)
