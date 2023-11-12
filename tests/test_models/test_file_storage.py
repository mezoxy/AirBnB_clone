#!/usr/bin/python3
"""this is test file storage"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """all test of this class is here"""

    def setUp(self):
        self.instt = FileStorage()

    def test_instante(self):
        self.assertIsInstance(self.instt, FileStorage)

    def test_all(self):
        obj = self.instt.all()
        self.assertIsInstance(obj, dict)

    def test_new(self):
        obj = BaseModel()
        self.instt.new(obj)
        all_objects = self.instt.all()
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.assertIn(key, all_objects)

    def test_save(self):
        obj = BaseModel()
        self.instt.new(obj)
        self.instt.save()
        all_objects = self.instt.all()
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.assertIn(key, all_objects)

if __name__ == "__main__":
    unittest.main()
