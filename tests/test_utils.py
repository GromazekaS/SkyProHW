import json
from unittest.mock import mock_open, patch

from src.utils import calculate_transaction_amount, get_transactions_from_file


def test_get_transactions_from_valid_file(transactions_test):
    mock_data = json.dumps(transactions_test)
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = get_transactions_from_file("dummy_path.json")
        assert result == transactions_test


def test_get_transactions_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError()):
        result = get_transactions_from_file("not_found.json")
        assert result == []


def test_get_transactions_invalid_json():
    with patch("builtins.open", mock_open(read_data="INVALID_JSON")), \
         patch("json.load", side_effect=json.JSONDecodeError("msg", "", 0)):
        result = get_transactions_from_file("invalid.json")
        assert result == []


def test_get_transactions_invalid_structure():
    bad_structure = json.dumps({"not": "a list"})
    with patch("builtins.open", mock_open(read_data=bad_structure)):
        result = get_transactions_from_file("bad_struct.json")
        assert result == []


test = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
}


@patch('src.utils.convert_currency')
def test_calculate_transaction_amount(mock_convert_currency):
    mock_convert_currency.return_value = 9265.7461
    assert calculate_transaction_amount(test, 'RUB') == 9265.7461

    mock_convert_currency.assert_called_once_with(*('8221.37', 'USD', 'RUB'))
