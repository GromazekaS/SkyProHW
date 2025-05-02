import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_currency(amount: str, form_currency: str, to_currency: str) -> float:
    """Вернуть сумму после конвертации по текущему курсу на https://api.apilayer.com"""
    # Для возможности тестирования приходится присвоение api-ключа делать внутри функции,
    # иначе придется светить его в тестах
    apilayer_api_key = os.getenv("API_KEY")

    url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={form_currency}&amount={amount}"

    headers = {
        "apikey": apilayer_api_key
    }
    payload : dict[str, str] = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()
    # {
    # 'success': True,
    # 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 100},
    # 'info': {'timestamp': 1746107344, 'quote': 92.657461},
    # 'result': 9265.7461}
    print(f'Статус запроса курса конвертации: {status_code}')
    print(f'Результат запроса: {result}')
    return float(result["result"])
