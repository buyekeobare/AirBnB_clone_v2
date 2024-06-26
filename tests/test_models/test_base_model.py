i#!/usr/bin/python3
"""
This is defines unittests for BaseModel class (models/base_model.py).
"""
import unittest
from models.base_model import BaseModel
from models import storage
import datetime
from time import sleep
import os


class TestBaseModel_init(unittest.TestCase):
    """Testing instantiation of BaseModel class."""

    # Testing type
    def test_type(self):
        bm = BaseModel()
        self.assertEqual(BaseModel, type(bm))

    def test_type_id(self):
        bm = BaseModel()
        self.assertEqual(str, type(bm.id))

    def test_type_created_at(self):
        bm = BaseModel()
        self.assertEqual(datetime.datetime, type(bm.created_at))

    def test_type_update_at(self):
        bm = BaseModel()
        self.assertEqual(datetime.datetime, type(bm.updated_at))

    # Testing id
    def test_unique_id(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    # Testing dates
    def test_consecutive_created_at(self):
        bm1 = BaseModel()
        sleep(0.02)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_consecutive_updated_at(self):
        bm1 = BaseModel()
        sleep(0.02)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    # Testing new attributes creation
    def test_new_attr(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 89
        self.assertTrue(hasattr(bm, "name") and hasattr(bm, "my_number"))

    # Test update storage variable
    def test_bm_updated_storage(self):
        bm = BaseModel()
        bm_key = "BaseModel." + bm.id
        keys = storage.all().keys()
        self.assertTrue(bm_key in keys)


class TestBaseModel_str(unittest.TestCase):
    """Testing __str__ method of BaseModel class"""

    def test_empty_input_str(self):
        bm = BaseModel()
        bm_str = str(bm)

        part1 = "[BaseModel] ("
        len_part1 = len(part1) + len(bm.id) + 2
        real1 = bm_str[: len_part1]
        exp1 = part1 + bm.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(bm_str[len_part1:])
        exp2 = bm.__dict__
        self.assertEqual(exp2, real2)

    def test_new_attr_str(self):
        bm = BaseModel()
        bm.name = "Holberton"
        bm.my_number = 89
        bm_str = str(bm)

        part1 = "[BaseModel] ("
        len_part1 = len(part1) + len(bm.id) + 2
        real1 = bm_str[: len_part1]
        exp1 = part1 + bm.id + ") "
        self.assertEqual(exp1, real1)

        real2 = eval(bm_str[len_part1:])
        exp2 = bm.__dict__
        self.assertEqual(exp2, real2)


class TestBaseModel_save(unittest.TestCase):
    """Testing save method of BaseModel class"""

    @classmethod
    def clean(self):
        """Remove 'file.json'"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_update_date(self):
        bm = BaseModel()
        date1 = bm.updated_at
        sleep(0.02)
        bm.save()
        date2 = bm.updated_at
        self.assertLess(date1, date2)

    def test_save_update_file(self):
        TestBaseModel_save.clean()
        bm = BaseModel()
        bm.save()
        bm_key = "BaseModel." + bm.id
        with open("file.json", "r") as file:
            json_text = file.read()
        self.assertTrue(bm_key in json_text)
        TestBaseModel_save.clean()


class TestBaseModel_to_dict(unittest.TestCase):
    """Testing to_dict method of BaseModel class"""

    def test_class_item(self):
        bm = BaseModel()
        bm_dict = bm.to_dict()
        real = bm_dict["__class__"]
        exp = "BaseModel"

    def test_created_at_format(self):
        bm = BaseModel()
        bm.created_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)
        bm_dict = bm.to_dict()
        real = bm_dict["created_at"]
        exp = "2024-06-28T21:05:54.119427"
        self.assertEqual(exp, real)

    def test_update_at_format(self):
        bm = BaseModel()
        bm.updated_at = datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
        bm_dict = bm.to_dict()
        real = bm_dict["updated_at"]
        exp = "2024-06-28T21:05:54.119572"
        self.assertEqual(exp, real)

    def test_empty_input_format(self):
        bm = BaseModel()
        bm.created_at = datetime.datetime(2024, 6, 28, 21, 5, 54, 119427)
        bm.updated_at = datetime.datetime(202024, 6, 28, 21, 5, 54, 119572)
        real = bm.to_dict()
        exp = {
            '__class__': 'BaseModel',
            'updated_at': '2024-06-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2024-06-28T21:05:54.119427'}

    def test_new_attr_format(self):
        bm = BaseModel()
        bm.created_at = datetime.datetime(2024, 6, 28, 21, 5, 54, 119427)
        bm.updated_at = datetime.datetime(2024, 6, 28, 21, 5, 54, 119572)
        bm.name = "Holberton"
        bm.my_number = "89"
        real = bm.to_dict()
        exp = {
            'my_number': 89,
            'name': 'Holberton',
            '__class__': 'BaseModel',
            'updated_at': '2024-06-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2024-06-28T21:05:54.119427'}


class TestBaseModel_kwargs_input(unittest.TestCase):
    """Test kwargs inputs for __init__ inputs"""

    def test_correct_dict_input(self):
        bm1 = BaseModel()
        bm1.created_at = datetime.datetime(2024, 6, 28, 21, 5, 54, 119427)
        bm1.updated_at = datetime.datetime(2024, 6, 28, 21, 5, 54, 119572)
        bm1.name = "Holberton"
        bm1.my_number = "89"
        bm1_dict = bm1.to_dict()

        bm2 = BaseModel(**bm1_dict)
        bm2_dict = bm2.to_dict()

        self.assertEqual(bm1_dict, bm2_dict)
        self.assertEqual(datetime.datetime, type(bm2.created_at))
        self.assertFalse(bm1 is bm2)

    def test_kwargs_all_inputs(self):
        cy_date = '2024-06-28T21:05:54.119427'
        us_date = '2024-06-28T21:05:54.119572'
        id_val = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        bm = BaseModel(
            id=id_val,
            created_at=cy_date,
            updated_at=us_date,
            name="Holberton")
        real = bm.to_dict()
        exp = {
            '__class__': 'BaseModel',
            'updated_at': '224-06-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2024-06-28T21:05:54.119427',
            'name': 'Holberton'}
        self.assertEqual(exp, real)

    def test_kwargs_id_create_at(self):
        cy_date = '2024-06-28T21:05:54.119427'
        id_val = "hola"
        bm = BaseModel(id=id_val, created_at=cy_date)
        bm.updated_at = datetime.datetime(2024, 6, 28, 21, 5, 54, 119573)
        real = bm.to_dict()
        exp = {
            '__class__': 'BaseModel',
            'updated_at': '2024-06-28T21:05:54.119573',
            'id': 'hola',
            'created_at': '2024-06-28T21:05:54.119427'}
        self.assertEqual(exp, real)

    def test_args_input_unused(self):
        bm = BaseModel("element")
        self.assertNotIn("element", bm.__dict__.values())

    def test_args_kwargs_input(self):
        cy_date = '2024-06-28T21:05:54.119427'
        us_date = '2024-06-28T21:05:54.119572'
        id_val = "b6a6e15c-c67d-4312-9a75-9d084935e579"
        bm = BaseModel(34, id=id_val, created_at=cy_date, updated_at=us_date)
        real = bm.to_dict()
        exp = {
            '__class__': 'BaseModel',
            'updated_at': '2024-06-28T21:05:54.119572',
            'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
            'created_at': '2024-06-28T21:05:54.119427'}
        self.assertEqual(exp, real)
