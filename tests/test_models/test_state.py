#!/usr/bin/python3
"""state class test"""
import unittest
from datetime import datetime
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """all test"""

    def setUp(self):
        self.state = State()

    def test_inst(self):
        self.assertIsInstance(State(), BaseModel)
        self.assertIsInstance(self.state, State)

    def test_element_dictio(self):
        self.assertEqual(type(self.state.id), str)
        self.assertEqual(type(self.state.created_at), datetime)
        self.assertEqual(type(self.state.updated_at), datetime)

    def test_id(self):
        self.state2 = State()
        self.assertNotEqual(self.state.id, self.state2.id)

    def test_time(self):
        self.assertNotEqual(self.state.updated_at, self.state.created_at)

    def test_nokwvalue(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
