import os
from unittest.mock import MagicMock, Mock, patch

from src.external_api import convert_currency, calculate_transaction_amount


@patch("requests.request")
# @patch('os.getenv')
# def test_convert_currency(mock_getenv, mock_request):
def test_convert_currency(mock_request: MagicMock) -> None:
    mock_request.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 100},
        "info": {"timestamp": 1746107344, "quote": 92.657461},
        "result": 9265.7461,
    }
    mock_getenv = Mock(return_value="012345")
    os.getenv = mock_getenv
    #    mock_getenv.return_value = '012345'
    assert convert_currency("100", "EUR", "RUB") == 9265.7461
    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/currency_data/convert?to=RUB&from=EUR&amount=100",
        headers={"apikey": mock_getenv.return_value},
        data={},
    )


test = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


@patch("src.external_api.convert_currency")
def test_calculate_transaction_amount(mock_convert_currency: MagicMock) -> None:
    mock_convert_currency.return_value = 9265.7461
    assert calculate_transaction_amount(test, "RUB") == 9265.7461

    mock_convert_currency.assert_called_once_with(*("8221.37", "USD", "RUB"))
