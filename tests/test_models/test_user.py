#!/usr/bin/python3
"""user.py test case"""

from models.base_model import BaseModel
from models.user import user
import unittest
from datetime import datetime


class test_userclass(unittest.TestCase):
    """class user test"""

    def setUp(self):
        self.user = User()

    def test_isnt(self):
        self.assertIsInstance(user, User)

    def test_sub(self):
        self.assertTrue(issubclass(User, BaseModel)

    def test_existe(self):
        self.user = User()
        self.user.first_name = "Betty"
        self.user.last_name = "Bar"
        self.user.email = "airbnb@mail.com"
        self.user.password = "root"
        self.user.save()
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.email), str)
        self.assertTrue(hasattr(user, "last_name"))
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_dictionnarry(self):
        self.assertEqual(type(user.to__dict), dict)

    def test_attr(self):
        self.assertTrue("email" in self.user.__dict__)
        self.assertTrue("first_name" in self.user.__dict__)
        self.assertTrue("password" in self.user.__dict__)
        self.assertTrue("last_name" in self.user.__dict__)


if __name__ = "__main__"
    unittest.main()
