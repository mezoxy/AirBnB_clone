#!/usr/bin/python3
"""this is test file of place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class testplace(unittest.TestCase):
    """test case of place class principale"""

    def setUp(self):
        self.pc = Place()

    def test_type(self):
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(isinstance(self.pc, Place))

    def test_ttr(self):
        self.assertTrue(hasattr(self.pc, 'id'))
        self.assertTrue(hasattr(self.pc, 'created_at'))
        self.assertTrue(hasattr(self.pc, 'updated_at'))
        self.assertTrue(hasattr(self.pc, 'latitude'))
        self.assertTrue(hasattr(self.pc, 'longitude'))
        self.assertTrue(hasattr(self.pc, 'amenity_ids'))
        self.assertTrue(hasattr(self.pc, 'price_by_night'))
        self.assertTrue(hasattr(self.pc, 'max_guest'))
        self.assertTrue(hasattr(self.pc, 'number_bathrooms'))
        self.assertTrue(hasattr(self.pc, 'number_rooms'))
        self.assertTrue(hasattr(self.pc, 'description'))

    def test_dicto(self):
        self.assertTrue('id' in self.pc.__dict__)
        self.assertTrue('updated_at' in self.pc.__dict__)
        self.assertTrue('created_at' in self.pc.__dict__)


if __name__ == '__main__':
    unittest.main()
