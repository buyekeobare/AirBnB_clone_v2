#!/usr/bin/python3
"""
This model defines unittests for Place class (models/place.py).
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage
import datetime
from time import sleep
import os


class TestPlace(unittest.TestCase):
    """Testing instantiation of Place class."""

    # Testing type
    def test_type(self):
        pl = Place()
        self.assertEqual(Place, type(pl))

    def test_type_public_attr(self):
        pl = Place()
        self.assertEqual(str, type(pl.id))
        self.assertEqual(str, type(pl.city_id))
        self.assertEqual(str, type(pl.user_id))
        self.assertEqual(str, type(pl.name))
        self.assertEqual(str, type(pl.description))
        self.assertEqual(int, type(pl.number_rooms))
        self.assertEqual(int, type(pl.number_bathrooms))
        self.assertEqual(int, type(pl.max_guest))
        self.assertEqual(int, type(pl.price_by_night))
        self.assertEqual(float, type(pl.latitude))
        self.assertEqual(float, type(pl.longitude))
        self.assertEqual(list, type(pl.amenity_ids))

    def test_type_created_at(self):
        pl = Place()
        self.assertEqual(datetime.datetime, type(pl.created_at))

    def test_type_update_at(self):
        pl = Place()
        self.assertEqual(datetime.datetime, type(pl.updated_at))

    # Testing id
    def test_unique_id(self):
        pl1 = Place()
        pl2 = Place()
        self.assertNotEqual(pl1.id, pl2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        pl1 = Place()
        sleep(0.02)
        pl2 = Place()
        self.assertLess(pl1.created_at, pl2.created_at)

    def test_consecutive_updated_at(self):
        pl1 = Place()
        sleep(0.02)
        pl2 = Place()
        self.assertLess(pl1.updated_at, pl2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        pl = Place()
        pl.name = "Holberton"
        pl.email = "janesmith@gmail.com"
        self.assertTrue(hasattr(pl, "name") and hasattr(pl, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        pl = Place()
        pl_key = "Place." + pl.id
        keys = storage.all().keys()
        self.assertTrue(pl_key in keys)
