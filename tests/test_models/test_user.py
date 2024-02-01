#!/usr/bin/python3
"""
Unittest for user class
"""
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """Tests user class"""

    usr = User()

    def test_cls_exst(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.usr)), "<class 'models.user.User'>")

    def test_usr_inherit(self):
        """test if User inhertis from BaseModel"""
        self.assertIsInstance(self.usr, User)

    def testGotAtt(self):
        """verify if attributes are existing"""
        self.assertTrue(hasattr(self.usr, 'email'))
        self.assertTrue(hasattr(self.usr, 'password'))
        self.assertTrue(hasattr(self.usr, 'first_name'))
        self.assertTrue(hasattr(self.usr, 'last_name'))
        self.assertTrue(hasattr(self.usr, 'id'))
        self.assertTrue(hasattr(self.usr, 'created_at'))
        self.assertTrue(hasattr(self.usr, 'updated_at'))

    def test_att_type(self):
        """tests if type of the attribute corresponds to the one in class"""
        self.assertIsInstance(self.usr.first_name, str)
        self.assertIsInstance(self.usr.last_name, str)
        self.assertIsInstance(self.usr.email, str)
        self.assertIsInstance(self.usr.password, str)
        self.assertIsInstance(self.usr.id, str)
        self.assertIsInstance(self.usr.created_at, datetime.datetime)
        self.assertIsInstance(self.usr.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
