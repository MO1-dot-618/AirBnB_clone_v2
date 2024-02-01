#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for State class."""

    def test_id_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_unique_ids(self):
        A1 = State()
        A2 = State()
        self.assertNotEqual(A1.id, A2.id)

    def test_datetime(self):
        A1 = State()
        sleep(0.1)
        A2 = State()
        self.assertNotEqual(A1.created_at, A2.created_at)


class TestState_to_dict(unittest.TestCase):
    """Unittests of to_dict method"""

    def test_dict_type(self):
        A = State()
        self.assertTrue(dict, type(A.to_dict()))

    def test_keys_attributes(self):
        A = State()
        A.my_number = 98
        self.assertIn("id", A.to_dict())
        self.assertIn("my_number", A.to_dict())

    def test_no_arg(self):
        A = State()
        with self.assertRaises(TypeError):
            A.to_dict(None)


class TestState_save(unittest.TestCase):
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
        A = State()
        sleep(0.1)
        ua = A.updated_at
        A.save()
        self.assertLess(ua, A.updated_at)

    def test_arg(self):
        A = State()
        with self.assertRaises(TypeError):
            A.save(None)

    def test_file(self):
        A = State()
        A.save()
        with open("file.json", "r") as f:
            self.assertIn("State." + A.id, f.read())


if __name__ == "__main__":
    unittest.main()
