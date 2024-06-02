#!/usr/bin/python3

"""
Testing module for utils module
"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):

	def test_access_nested_map(self):
		""" Testing the access_nested_map function"""
		self.assertEqual(access_nested_map({"a": 1}, path=("a",)), 1)
		self.assertEqual(access_nested_map({"a": {"b": 2}}, path=("a",)), {'b': 2})
