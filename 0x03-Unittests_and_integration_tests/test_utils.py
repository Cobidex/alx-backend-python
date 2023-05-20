#!usr/bin/env python3
'''
contains the test class TestAccessNestedMap
'''
import unittest
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
    def test_access_nested_map(self, collection, keys, value):
        '''tests the access_nested_map method'''
        self.assertEqual(access_nested_map(collection, keys), value)

if __name__ == '__main__':
    unittest.run()
