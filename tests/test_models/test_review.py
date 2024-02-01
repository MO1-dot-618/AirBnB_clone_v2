#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview_instantiation
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Unittests for Review class."""

    def test_id_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_unique_ids(self):
        A1 = Review()
        A2 = Review()
        self.assertNotEqual(A1.id, A2.id)

    def test_datetime(self):
        A1 = Review()
        sleep(0.1)
        A2 = Review()
        self.assertNotEqual(A1.created_at, A2.created_at)

    def test_public_class_attributes(self):
        rv = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rv))
        self.assertNotIn("place_id", rv.__dict__)
        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(rv))
        self.assertNotIn("user_id", rv.__dict__)
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rv))
        self.assertNotIn("text", rv.__dict__)


class TestReview_to_dict(unittest.TestCase):
    """Unittests of to_dict method"""

    def test_dict_type(self):
        A = Review()
        self.assertTrue(dict, type(A.to_dict()))

    def test_keys_attributes(self):
        A = Review()
        A.my_number = 98
        self.assertIn("id", A.to_dict())
        self.assertIn("my_number", A.to_dict())

    def test_no_arg(self):
        A = Review()
        with self.assertRaises(TypeError):
            A.to_dict(None)


class TestReview_save(unittest.TestCase):
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
        A = Review()
        sleep(0.1)
        ua = A.updated_at
        A.save()
        self.assertLess(ua, A.updated_at)

    def test_arg(self):
        A = Review()
        with self.assertRaises(TypeError):
            A.save(None)

    def test_file(self):
        A = Review()
        A.save()
        with open("file.json", "r") as f:
            self.assertIn("Review." + A.id, f.read())


if __name__ == "__main__":
    unittest.main()
