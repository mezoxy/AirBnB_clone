#!/usr/bin/python3
"""testcase for city.py"""

import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
import uuid


class Test_class(unittest.TestCase):
    """class city test"""

    def setUp(self):
        self.sity = City()
        self.A = self.sity.__dict__
        self.sity.state_id = str(uuid.uuid4())
        self.sity.name = "okokok"

    def test_type(self):
        self.assertTrue(isinstance(self.sity, City))

    def test_subclas(self):
        self.assertTrue(issubclass(City, BaseModel))

    def test_id(self):
        for element in self.A.items():
            self.assertEqual(type(self.sity.state_id), str)
            self.assertEqual(type(self.sity.updated_at), datetime)
            self.assertEqual(type(self.sity.created_at), datetime)
            self.assertEqual(type(self.sity.name), str)

    def test_check_var(self):
        self.sity.number = 89
        self.assertFalse('state_d' in self.sity.__dict__)
        self.assertTrue('created_at' in self.A)
        self.assertTrue('updated_at' in self.A)
        self.assertTrue('number' in self.A)
        self.assertTrue('name' in self.A)


if __name__ == '__main__':
    unittest.main()
