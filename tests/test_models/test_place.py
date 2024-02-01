#!/usr/bin/python3
"""
Unittest for place.py
"""
import unittest
import models
from models.place import Place
import datetime


class TestPlace(unittest.TestCase):
    """Tests instances for place"""

    pl = Place()

    def test_cl_exst(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.pl)), "<class 'models.place.Place'>")

    def test_usr_inherit(self):
        """test if Place inherits from BaseModel"""
        self.assertIsInstance(self.pl, Place)

    def testGotAtt(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.pl, 'city_id'))
        self.assertTrue(hasattr(self.pl, 'user_id'))
        self.assertTrue(hasattr(self.pl, 'name'))
        self.assertTrue(hasattr(self.pl, 'description'))
        self.assertTrue(hasattr(self.pl, 'number_rooms'))
        self.assertTrue(hasattr(self.pl, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pl, 'max_guest'))
        self.assertTrue(hasattr(self.pl, 'price_by_night'))
        self.assertTrue(hasattr(self.pl, 'latitude'))
        self.assertTrue(hasattr(self.pl, 'longitude'))
        self.assertTrue(hasattr(self.pl, 'amenity_ids'))
        self.assertTrue(hasattr(self.pl, 'id'))
        self.assertTrue(hasattr(self.pl, 'created_at'))
        self.assertTrue(hasattr(self.pl, 'updated_at'))

    def test_types(self):
        """tests attribute type"""
        self.assertIsInstance(self.pl.city_id, str)
        self.assertIsInstance(self.pl.user_id, str)
        self.assertIsInstance(self.pl.name, str)
        self.assertIsInstance(self.pl.description, str)
        self.assertIsInstance(self.pl.number_rooms, int)
        self.assertIsInstance(self.pl.number_bathrooms, int)
        self.assertIsInstance(self.pl.max_guest, int)
        self.assertIsInstance(self.pl.price_by_night, int)
        self.assertIsInstance(self.pl.latitude, float)
        self.assertIsInstance(self.pl.longitude, float)
        self.assertIsInstance(self.pl.amenity_ids, list)
        self.assertIsInstance(self.pl.id, str)
        self.assertIsInstance(self.pl.created_at, datetime.datetime)
        self.assertIsInstance(self.pl.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
