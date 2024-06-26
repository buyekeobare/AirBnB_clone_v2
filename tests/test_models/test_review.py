#!/usr/bin/python3
"""
This model defines unittests for Review class (models/review.py)
"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage
import datetime
from time import sleep
import os


class TestReview(unittest.TestCase):
    """Testing instantiation of User class."""

    # Testing type
    def test_type(self):
        rev = Review()
        self.assertEqual(Review, type(rev))

    def test_type_public_attr(self):
        rev = Review()
        self.assertEqual(str, type(rev.id))
        self.assertEqual(str, type(rev.place_id))
        self.assertEqual(str, type(rev.user_id))
        self.assertEqual(str, type(rev.text))

    def test_type_created_at(self):
        rev = Review()
        self.assertEqual(datetime.datetime, type(rev.created_at))

    def test_type_update_at(self):
        rev = Review()
        self.assertEqual(datetime.datetime, type(rev.updated_at))

    # Testing id
    def test_unique_id(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        rev1 = Review()
        sleep(0.02)
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_consecutive_updated_at(self):
        rev1 = Review()
        sleep(0.02)
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        rev = Review()
        rev.name = "Holberton"
        rev.email = "janesmith@gmail.com"
        self.assertTrue(hasattr(rev, "name") and hasattr(rev, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        rev = Review()
        rev_key = "Review." + rev.id
        keys = storage.all().keys()
        self.assertTrue(rev_key in keys)
