import os
import unittest
from unittest.mock import MagicMock, Mock, patch

import requests
from dotenv import load_dotenv

from src.external_api import currency_conversion

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")


class TestConvertToRub(unittest.TestCase):

    @patch("requests.get")
    def test_convert_usd_to_rub(self, mock_get: MagicMock) -> None:
        mock_get.return_value.json.return_value = {"result": 75.0}
        mock_get.return_value.status_code = 200

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}

        result = currency_conversion(transaction)
        self.assertEqual(result, 75.0)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1", headers={"apikey": API_KEY}
        )

    @patch("requests.get")
    def test_convert_eur_to_rub(self, mock_get: MagicMock) -> None:
        mock_get.return_value.json.return_value = {"result": 75.0}
        mock_get.return_value.status_code = 200

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "EUR"}}}

        result = currency_conversion(transaction)
        self.assertEqual(result, 85.0)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=1", headers={"apikey": API_KEY}
        )

    def test_convert_rub_to_rub(self) -> None:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "RUB"}}}

        result = currency_conversion(transaction)
        self.assertEqual(result, 100)

    def test_convert_other_currency_to_rub(self) -> None:
        transaction = {"operationAmount": {"amount": 100, "currency": {"code": "GBR"}}}

        result = currency_conversion(transaction)
        self.assertEqual(result, 0.0)

    @patch("requests.get")
    def test_api_failure(self, mock_get: MagicMock) -> None:
        mock_responce = Mock()
        mock_responce.raise_for_status.side_effect = requests.exceptions.RequestException(response=mock_responce)
        mock_get.return_value = mock_responce

        transaction = {"operationAmount": {"amount": 1, "currency": {"code": "USD"}}}

        result = currency_conversion(transaction)
        self.assertEqual(result, 0.0)
