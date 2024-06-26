#!/usr/bin/python3
"""
This define unittests for City class (models/city.py).
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage
import datetime
from time import sleep
import os


class TestCity(unittest.TestCase):
    """Testing instantiation of City class."""

    # Testing type
    def test_type(self):
        cy = City()
        self.assertEqual(City, type(cy))

    def test_type_public_attr(self):
        cy = City()
        self.assertEqual(str, type(cy.id))
        self.assertEqual(str, type(cy.state_id))
        self.assertEqual(str, type(cy.name))

    def test_type_created_at(self):
        cy = City()
        self.assertEqual(datetime.datetime, type(cy.created_at))

    def test_type_update_at(self):
        cy = City()
        self.assertEqual(datetime.datetime, type(cy.updated_at))

    # Testing id
    def test_unique_id(self):
        cy1 = City()
        cy2 = City()
        self.assertNotEqual(cy1.id, cy2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        cy1 = City()
        sleep(0.02)
        cy2 = City()
        self.assertLess(cy1.created_at, cy2.created_at)

    def test_consecutive_updated_at(self):
        cy1 = City()
        sleep(0.02)
        cy2 = City()
        self.assertLess(cy1.updated_at, cy2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        cy = City()
        cy.name = "Holberton"
        cy.email = "janesmith@gmail.com"
        self.assertTrue(hasattr(cy, "name") and hasattr(cy, "email"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        cy = City()
        cy_key = "City." + cy.id
        keys = storage.all().keys()
        self.assertTrue(cy_key in keys)
