#!/usr/bin/env python3
''' Test utils '''
import unittest
from unittest.mock import MagicMock, patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test for github org client"""
    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """Test for org"""
        mock_get_json.return_value = MagicMock(return_value=expected)
        org = GithubOrgClient(org_name)
        self.assertEqual(org.org(), expected)
        mock_get_json.assert_called_once_with(
            org.ORG_URL.format(org=org_name)
        )


if __name__ == '__main__':
    unittest.main()
