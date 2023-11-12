#!/usr/bin/python3
"""this file is about tests casses of base_model"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import re
import uuid


class TestBaseModel(unittest.TestCase):
    """test casses of class BaseModel"""

    def setUp(self):
        """test fixture setup"""

        self.inst1 = BaseModel()
        self.inst = BaseModel()
        self.inst.id = str(uuid.uuid4())

    def tearDown(self):
        """clean up code"""
        pass

    def test_id(self):
        self.assertTrue(hasattr(self.inst, "id"))

    # noqa
    def test_pattern(self):
        """
            test if inst matches a specific pattern
            defined by a regular expression
        """
        self.assertTrue(
                re.match(
                     r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-'
                     r'[89ab][a-f0-9]{3}-[a-f0-9]{12}$',
                     str(self.inst.id)))

    def test_uniqId(self):
        """check if too instance dont have the same id"""
        self.assertNotEqual(self.inst1.id, self.inst.id)

    def test_type(self):
        self.assertIsInstance(self.inst, BaseModel)
        self.assertIsInstance(self.inst.id, str)
        self.assertIsInstance(self.inst.created_at, datetime)
        self.assertIsInstance(self.inst.updated_at, datetime)

    def test_str_t(self):
        self.assertNotEqual(self.inst1.updated_at, self.inst.created_at)

    def test_str(self):
        self.assertEqual("[BaseModel] ({}) {}".format(
            self.inst.id, self.inst.__dict__), str(self.inst))

    def test_save(self):
        updated = self.inst1.updated_at
        self.inst1.save()
        updated1 = self.inst1.updated_at
        self.assertNotEqual(updated, updated1)

    def test_dect(self):
        self.assertTrue(type(self.inst.to_dict), dict)

    def test_dectt(self):
        self.inst.name = "ayoub"
        self.assertIn("name", self.inst.to_dict())

    def test_dectw(self):
        dect = {
                'id': self.inst.id,
                '__class__': 'BaseModel',
                'created_at': self.inst.created_at.isoformat(),
                'updated_at': self.inst.updated_at.isoformat()
                }
        self.assertEqual(self.inst.to_dict(), dect)

    def test_draise(self):
        with self.assertRaises(TypeError):
            self.inst.to_dict(None)

    def test_strrepr(self):
        self.inst = BaseModel(
                id=str(uuid.uuid4()),
                created_at=str(datetime.now()),
                updated_at=str(datetime.now()))
        repr_str = f"[BaseModel] ({self.inst.id})"
        repr_str += " {}: '{}',".format('{"id"', self.inst.id)
        repr_str += f" 'created_at': {repr(self.inst.created_at)},"
        repr_str += " 'updated_at': {}{}".format(
                repr(self.inst.updated_at), '}')
        self.assertEqual(str(self.inst), repr_str.replace('"', "'"))


if __name__ == '__main__':
    unittest.main()
