#!/usr/bin/env python3
'''
contains the test class TestAccessNestedMap
'''
import unittest
from typing import Any
from parameterized import parameterized
from utils import access_nested_map


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


if __name__ == "__main__":
    unittest.main()
