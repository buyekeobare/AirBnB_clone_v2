#!/usr/bin/python3
"""
This defines unittests for User class (models/user.py)
"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import datetime
from time import sleep
import os


class TestUsers(unittest.TestCase):
    """Testing instantiation of User class."""

    # Testing type
    def test_type(self):
        us = User()
        self.assertEqual(User, type(us))

    def test_type_id(self):
        us = User()
        self.assertEqual(str, type(us.id))

    def test_type_public_attr(self):
        us = User()
        self.assertEqual(str, type(us.email))
        self.assertEqual(str, type(us.password))
        self.assertEqual(str, type(us.first_name))
        self.assertEqual(str, type(us.last_name))

    def test_type_created_at(self):
        us = User()
        self.assertEqual(datetime.datetime, type(us.created_at))

    def test_type_update_at(self):
        us = User()
        self.assertEqual(datetime.datetime, type(us.updated_at))

    # Testing id
    def test_unique_id(self):
        us1 = User()
        us2 = User()
        self.assertNotEqual(us1.id, us2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        us1 = User()
        sleep(0.02)
        us2 = User()
        self.assertLess(us1.created_at, us2.created_at)

    def test_consecutive_updated_at(self):
        us1 = User()
        sleep(0.02)
        us2 = User()
        self.assertLess(us1.updated_at, us2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        us = User()
        us.name = "Holberton"
        us.my_number = "janesmith@gmail.com"
        self.assertTrue(hasattr(us, "name") and hasattr(us, "my_number"))
    
    def test_bm_updated_storage(self):
        us = User()
        us_key = "User." + us.id
        keys = storage.all().keys()
        self.assertTrue(us_key in keys)
