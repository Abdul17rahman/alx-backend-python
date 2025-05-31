#!/usr/bin/env python3


""" 
Client Testing Module
"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch


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


if __name__ == "__main__":
    unittest.main()
