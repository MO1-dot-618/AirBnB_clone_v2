#!/usr/bin/python3
""" Module of Unittests for FileStorage """
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import os
import json


class FileStorageTests(unittest.TestCase):
    """  File Storage Tests """

    t_model = BaseModel()

    def testClassInstance(self):
        """ Check instance """
        self.assertIsInstance(storage, FileStorage)

    def testSaveFunctionality(self):
        """ Test save and reload functions """
        self.t_model.name = "Super BaseModel"
        self.t_model.save()
        model_dict = self.t_model.to_dict()
        all_obj = storage.all()

        key = model_dict['__class__'] + "." + model_dict['id']
        self.assertEqual(key in all_obj, True)

    def testsave(self):
        """verify if JSON exists"""
        self.t_model.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertEqual(hasattr(FileStorage, '_FileStorage__file_path'), True)
        self.assertEqual(hasattr(FileStorage, '_FileStorage__objects'), True)


if __name__ == '__main__':
    unittest.main()
