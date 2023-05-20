#!/usr/bin/env python3
'''
contains the test class TestAccessNestedMap
'''
import unittest
from typing import Any
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    '''
    class containing test method for the utils.access_nested_map method
    '''
    @parameterized.expand([
        ({'a': 1}, ['a'], 1),
        ({'a': {'b': 2}}, ['a'], {'b': 2}),
        ({'a': {'b': 2}}, ['a', 'b'], 2)
        ])
    def test_access_nested_map(self, collection: dict,
                               keys: list, value: Any) -> None:
        '''tests the access_nested_map method'''
        self.assertEqual(access_nested_map(collection, keys), value)

    @parameterized.expand([
        ({}, ['a']),
        ({'a': 1}, ['a', 'b'])
        ])
    def test_access_nested_map_exception(self, collection: dict,
                                         keys: list) -> None:
        '''checks if the KeyError exception is raised'''
        self.assertRaises(KeyError, access_nested_map, collection, keys)


class TestGetJson(unittest.TestCase):
    '''
    contains methods to test the get_json methods of utils module
    '''
    @parameterized.expand([
        ("http://example.com", {'payload': True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests')
    def test_get_json(self, url: str, payload: dict, mock_requests,) -> dict:
        '''checks if expected json is retrieved'''
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = payload
        mock_requests.get.return_value = mock_response

        self.assertEqual(get_json(url), payload)


if __name__ == "__main__":
    unittest.main()
