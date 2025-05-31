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


if __name__ == "__main__":
    unittest.main()
