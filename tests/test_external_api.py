from unittest.mock import patch, Mock
import os
from src.external_api import convert_currency


@patch('requests.request')
# @patch('os.getenv')
# def test_convert_currency(mock_getenv, mock_request):
def test_convert_currency(mock_request):
    mock_request.return_value.json.return_value = {
        'success': True,
        'query': {'from': 'EUR', 'to': 'RUB', 'amount': 100},
        'info': {'timestamp': 1746107344, 'quote': 92.657461},
        'result': 9265.7461}
    mock_getenv = Mock(return_value = '012345')
    os.getenv = mock_getenv
#    mock_getenv.return_value = '012345'
    assert convert_currency(100, 'EUR', 'RUB') == 9265.7461
    mock_request.assert_called_once_with(
        'GET',
        'https://api.apilayer.com/currency_data/convert?to=RUB&from=EUR&amount=100',
        headers={'apikey': mock_getenv.return_value},
        data={}
    )
