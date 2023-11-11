#!/usr/bin/python3
"""testcase for city.py"""

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime


def test_class(unittest.TestCase):
    """class city test"""

    def setUp(self):
        self.sity = City()
        self.sity.__dict__ = A
        self.sity.state_id = str(uuid.uuid4)
        self.sity.name = "okokok"

    def test_type(self):
        self.assertTrue(isinstance(sity, City)

    def test_subclass(self):
        self.assertTrue(issubclass(City(), BaseModel)

    def test_id(self):
        for element in self.A.items():
                self.assertEqual(type(self.sity.stat_id), str)
                self.assertEqual(type(self.sity.updated_at), datetime)
                self.assertEqual(type(self.sity.created_at), datetime)
                self.assertEqual(type(self.sity.name), str)

    def test_check_var(self):
        self.sity.number = 89
        self.assertTrue('state_d' in self.city.__dict__)
        self.assertTrue('created_at' in A)
        self.assertTrue('updated_at' in A)
        self.assertTrue('number' in A)
        self.assertTrue('name' in A)

if __name__ = "__main__"
    unittest.main()
