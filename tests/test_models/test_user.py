#!/usr/bin/python3
"""user.py test case"""

from models.base_model import BaseModel
from models.user import User
import unittest
from datetime import datetime

class TestUserClass(unittest.TestCase):
    """class user test"""

    def setUp(self):
        self.user = User()

    def test_isnt(self):
        self.assertIsInstance(self.user, User)

    def test_sub(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_existe(self):
        self.user = User()
        self.user.first_name = "Betty"
        self.user.last_name = "Bar"
        self.user.email = "airbnb@mail.com"
        self.user.password = "root"
        self.user.save()
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.email), str)
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_dictionary(self):
        self.assertEqual(type(self.user.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
