#!/usr/bin/env python3

"""
Testing module for the utils module
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Testing access_nested_map() function for correct results."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Testing the access_nested method"""
        result = access_nested_map(nested_map, path)

        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Testing exception from the access_nested_method"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Testing get_json() function by mocking the results."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, payload, mock_obj):
        """ Testing the get_json method"""
        mock_response = MagicMock()
        mock_response.json.return_value = payload
        mock_obj.return_value = mock_response

        res = get_json(test_url)

        self.assertEqual(res, payload)

        mock_obj.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Testing Memoization functionality by mocking the results."""

    def test_memoize(self):
        """ Test Momoize function"""
        class TestClass:
            """ Testing class for memoization."""

            def a_method(self):
                """ Test method that will be memoized"""
                return 42

            @memoize
            def a_property(self):
                """ Memoization in action"""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_m:
            instance = TestClass()

            res1 = instance.a_property
            res2 = instance.a_property

            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)

            mock_m.assert_called_once()


if __name__ == "__main__":
    unittest.main()
