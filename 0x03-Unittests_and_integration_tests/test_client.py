#!/usr/bin/env python3
'''
contains the TestGithubOrgClient class
'''
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''
    contains methods for testing the GithubOrgClient class methods
    '''
    @parameterized.expand([
        ('google', {'payload': True}),
        ('abc', {'payload': True})
        ])
    @patch('client.get_json')
    def test_org(self, name: str, payload: dict, mock_get_json) -> None:
        '''test the return value of org method'''
        mock_get_json.return_value = payload
        t_client = GithubOrgClient(name)
        self.assertEqual(t_client.org, payload)
        mock_get_json.assert_called_once
