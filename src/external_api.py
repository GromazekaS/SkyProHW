import os
from dotenv import load_dotenv
import requests

load_dotenv()

apilayer_api_key = os.getenv("API_KEY")


def convert_currency(amount, form_currency, to_currency) -> float:
    """Вернуть сумму после конвертации по текущему курсу на https://api.apilayer.com"""
    url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={form_currency}&amount={amount}"

    payload = {}
    headers = {
        "apikey": apilayer_api_key
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()
    # {'success': True, 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 100}, 'info': {'timestamp': 1746107344, 'quote': 92.657461}, 'result': 9265.7461}
    print(f'Статус запроса курса конвертации: {status_code}')
    print(f'Результат запроса: {result}')
    return result["result"]
