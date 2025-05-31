#!/usr/bin/env python3


""" 
Client Testing Module
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """ This class Tests the Github Org Client class"""

    @parameterized.expand([
        ("google", {"name": "Google"}),
        ("abc", {"name": "ABC Corp"})
    ])
    @patch(f'{GithubOrgClient.__module__}.get_json')
    def test_org(self, client, expected, mock_obj):
        """ Test the org memoized results"""
        mock_obj.return_value = expected

        inst = GithubOrgClient(client)

        res = inst.org

        self.assertEqual(res, expected)

        mock_obj.assert_called_once_with(
            f"https://api.github.com/orgs/{client}")

    def test_public_repos_url(self):
        """Test public_repos_url returns the correct URL"""

        expected_url = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected_url}

        with patch.object(GithubOrgClient, "org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload

            client = GithubOrgClient("google")
            result = client._public_repos_url

            self.assertEqual(result, expected_url)
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns correct repo names"""

        expected_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = expected_payload

        with patch.object(
            GithubOrgClient,
            "_public_repos_url",
            new_callable=PropertyMock
        ) as mock_repos_url:
            mock_repos_url.return_value = "https://fake-url.com/orgs/repos"

            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://fake-url.com/orgs/repos")


if __name__ == "__main__":
    unittest.main()
