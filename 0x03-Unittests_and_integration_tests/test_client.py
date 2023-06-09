#!/usr/bin/env python3
'''
contains the TestGithubOrgClient class
'''
import unittest
from typing import Any
from unittest.mock import patch, PropertyMock, MagicMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from urllib.error import HTTPError


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", False),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    @patch('client.access_nested_map')
    def test_has_license(self, repo: dict, license_key: str,
                         value: bool, mock_access):
        '''
        test the has_license method
        '''
        mock_access.return_value = value
        t_client = GithubOrgClient("google")
        result = t_client.has_license(repo, license_key)
        self.assertEqual(result, value)


@parameterized_class(
        ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
        TEST_PAYLOAD
        )
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''
    contains method for the integration tests
    '''

    @classmethod
    def setUpClass(cls) -> None:
        '''
        executes before tests to start a patcher
        '''
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.my_side_effect

    @classmethod
    def tearDownClass(cls) -> None:
        '''
        stops the patcher after test is run
        '''
        cls.mock_get.stop()

    @classmethod
    def my_side_effect(cls, url: str) -> Any:
        '''
        modifies return value of mocked request.get
        '''
        response = MagicMock()
        if url == 'https://api.github.com/orgs/google':
            response.json.return_value = cls.org_payload
        elif url == 'https://api.github.com/orgs/google/repos':
            response.json.return_value = cls.repos_payload
        return response

    def test_public_repos(self):
        """
        Test the public_repos method
        """
        t_client = GithubOrgClient('google')
        repos: dict[str, Any] = t_client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        '''
        test the has_license method
        '''
        t_client = GithubOrgClient("google")
        repos: dict[str, Any] = t_client.public_repos(license='apache-2.0')
        self.assertEqual(repos, self.apache2_repos)
