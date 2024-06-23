import builtins
import unittest

import pytest

from unittest.mock import patch, mock_open, MagicMock

import requests

from src.external_api import currency_conversion
from src.utils import transaction_amount

import json

class TestGetTransaction(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='[{"transaction": "data1"}, {"transaction": "data2"}]')
    def test_transaction_amount_valid_file(self, mock_file: MagicMock) -> None:
        expected_data = [{"transaction": "data1"}, {"transaction": "data2"}]
        result = transaction_amount("fake_path.json")
        self.assertEqual(result, expected_data)
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open, read_data="{}")
    def test_transaction_amount_invalid_content(self, mock_file: MagicMock) -> None:
        result = transaction_amount("fake_path.json")
        self.assertEqual(result, [])
        mock_file.assert_called_once_with("fake_path.json", "r", encoding="utf-8")
