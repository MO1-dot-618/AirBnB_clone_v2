"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for BaseModel class."""

    def test_id_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids(self):
        A1 = BaseModel()
        A2 = BaseModel()
        self.assertNotEqual(A1.id, A2.id)

    def test_datetime(self):
        A1 = BaseModel()
        sleep(0.1)
        A2 = BaseModel()
        self.assertNotEqual(A1.created_at, A2.created_at)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests of to_dict method"""

    def test_dict_type(self):
        A = BaseModel()
        self.assertTrue(dict, type(A.to_dict()))

    def test_keys_attributes(self):
        A = BaseModel()
        A.my_number = 98
        self.assertIn("id", A.to_dict())
        self.assertIn("my_number", A.to_dict())

    def test_no_arg(self):
        A = BaseModel()
        with self.assertRaises(TypeError):
            A.to_dict(None)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for save() method"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save(self):
        A = BaseModel()
        sleep(0.1)
        ua = A.updated_at
        A.save()
        self.assertLess(ua, A.updated_at)

    def test_arg(self):
        A = BaseModel()
        with self.assertRaises(TypeError):
            A.save(None)

    def test_file(self):
        A = BaseModel()
        A.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + A.id, f.read())


if __name__ == "__main__":
    unittest.main()
