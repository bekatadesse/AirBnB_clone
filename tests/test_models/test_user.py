#!/usr/bin/python3
"""
Test suite for the User class in models.user
"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Tests instances and methods from user class"""
   u = User()
  def test_class_exists(self):
        """tests if class exists"""
        self.assertEqual(str(type(self.u)), "<class 'models.user.User'>")

    def test_class_attrs(self):
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
