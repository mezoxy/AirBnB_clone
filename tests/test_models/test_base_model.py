#!/usr/bin/env python3
"""this file is about tests casses of base_model"""

from models.base_model import BaseModel
from datetime import datetime
import unittest
import re """this is for regex"""


class TestBaseModel(unittest.TestCase):
    """test casses of class BaseModel"""

    def setUp(self):
        """test fixture setup"""

        self.inst1 = BaseModel()
        self.inst = BaseModel()

    def tearDown(self):
        """clean up code"""
        pass

    def test_id(self):
        self.assertTrue(hasattr(self.inst, "id"))

    def test_pattern(self):
        """test if inst matches a specific pattern defined by a regular expression"""
        self.assertTrue(re.match((r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}$'), str(inst.id)))
        
    def test_uniqId(self):
        """check if too instance dont have the same id"""
        self.assertNotEqual(inst1.id, inst.id)
        
    def test_type(self):
        self.assertIsInstance(inst, BaseModel)
        self.assertIsInstance(inst.id, str)
        self.assertIsInstance(inst.created_at, datetime)
        self.assertIsInstance(inst.updated_at, datetime)

    def test_str_t(self):
        self.assertNotEqual(inst1.updated_at, inst.created_at)

    def test_str(self):
        self.assertEqual("[{}] {} {}".format(self.__class__.__name__, self.id,
            self.__dict__), str(self.inst1))

    def test_save(self):
        updated = inst1.updated_at
        inst1.save()
        updated1 = inst1.updated_at
        self.assertNotEqual(updated, updated1)

    def test_dect(self):
        self.assertIsInstance(self.inst.to_dict, dict)

    def test_dectt(self):
        inst.name = "ayoub"
        self.assertIn("name", inst.to_dict())

    def test_dectw(self):
        dect = {
                'id' = '123456789',
                '__class__': 'BaseModel'
                'created_at': datetime.now().isoormat(),
                'updated_at': datetime.now().isoormat()
                }
        self.assertEqual(inst.to_dict(), dect)

    def test_draise(sel):
        with self.assertRaises(TypeError):
            inst.to_dict(None)

    def test_strrepr(self):
        inst = BaseModel(id=str(uuid.uuid4()), created_at=datetime.now(), updated_at=datetime.now())
        repr_str = f"[{self.__class__.__name__}] ({inst.id})\n"
        repr_str += f"  'id': '{inst.id}'\n"
        repr_str += f"  'created_at': {repr(inst.created_at)}\n"
        repr_str += f"  'updated_at': {repr(inst.updated_at)}"

        self.assertEqual(str(inst), repr_str)

if __name__ == "__main__":
    unittest.main()
