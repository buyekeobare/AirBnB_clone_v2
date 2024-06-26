I#!/usr/bin/python3
"""
This model defines unittests for State class (models/state.py).
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
import datetime
from time import sleep
import os


class TestState(unittest.TestCase):
    """Testing instantiation of State class."""

    # Testing type
    def test_type(self):
        st = State()
        self.assertEqual(State, type(st))

    def test_type_public_attr(self):
        st = State()
        self.assertEqual(str, type(st.id))
        self.assertEqual(str, type(st.name))

    def test_type_created_at(self):
        st = State()
        self.assertEqual(datetime.datetime, type(st.created_at))

    def test_type_update_at(self):
        st = State()
        self.assertEqual(datetime.datetime, type(st.updated_at))

    # Testing id
    def test_unique_id(self):
        st1 = State()
        st2 = State()
        self.assertNotEqual(st1.id, st2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        st1 = State()
        sleep(0.02)
        st2 = State()
        self.assertLess(st1.created_at, st2.created_at)

    def test_consecutive_updated_at(self):
        st1 = State()
        sleep(0.02)
        st2 = State()
        self.assertLess(st1.updated_at, st2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        st = State()
        st.name = "Holberton"
        st.email = "janesmith@gmail.com"
        self.assertTrue(hasattr(st, "name") and hasattr(st, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        st = State()
        st_key = "State." + st.id
        keys = storage.all().keys()
        self.assertTrue(st_key in keys)

