#!/usr/bin/env python3
'''
contains the TestGithubOrgClient class
'''
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        '''
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        '''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            url = "www.google.com"
            mock_org.return_value = {'repos_url': url}
            t_client = GithubOrgClient('google')
            self.assertEqual(t_client._public_repos_url, url)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        '''
        Test that the list of repos is what is expected
        Test that the mocked property and the mocked get_json was called once
        '''
        mock_get_json.return_value = [{"name": "repo1"}]
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pur:
            url = 'www.google.com'
            mock_pur.return_value = url
            t_client = GithubOrgClient("google")
            result = t_client.public_repos()
            self.assertEqual(result, ['repo1'])
            mock_pur.assert_called_once
            mock_get_json.assert_called_once
