
"""Test suite for the State class of the models.state module"""
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    s = State()

    def setUp(self):
        self.state = State()

    def test_state_is_a_subclass_of_basemodel(self):
        """test if State is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attr_is_a_class_attr(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.state, "name"))

    def testHasAttributes(self):
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.s, 'name'))
        self.assertTrue(hasattr(self.s, 'id'))
        self.assertTrue(hasattr(self.s, 'created_at'))
        self.assertTrue(hasattr(self.s, 'updated_at'))
        
if __name__ == '__main__':
    unittest.main()
