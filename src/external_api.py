import os

import requests
from dotenv import load_dotenv
from src.logger import logger_setup

logger = logger_setup("external_api")

load_dotenv()


def convert_currency(amount: str, form_currency: str, to_currency: str) -> float:
    """Вернуть сумму после конвертации по текущему курсу на https://api.apilayer.com"""
    # Для возможности тестирования приходится присвоение api-ключа делать внутри функции,
    # иначе придется светить его в тестах
    apilayer_api_key = os.getenv("API_KEY")

    url = f"https://api.apilayer.com/currency_data/convert?to={to_currency}&from={form_currency}&amount={amount}"

    headers = {"apikey": apilayer_api_key}
    payload: dict[str, str] = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = response.json()
    # {
    # 'success': True,
    # 'query': {'from': 'EUR', 'to': 'RUB', 'amount': 100},
    # 'info': {'timestamp': 1746107344, 'quote': 92.657461},
    # 'result': 9265.7461}
    print(f"Статус запроса курса конвертации: {status_code}")
    print(f"Результат запроса: {result}")
    return float(result["result"])


def calculate_transaction_amount(transaction: dict, dist_currency: str = "RUB") -> float:
    """Пересчет суммы транзакции в заданной валюте"""
    # pprint(transaction)
    amount = transaction["operationAmount"]["amount"]
    from_cur = transaction["operationAmount"]["currency"]["code"]
    if from_cur == dist_currency:
        res = float(amount)
        print(f"Конвертация не требуется. {amount} {dist_currency}")
    else:
        logger.info(f"Отправляем запрос на конвертацию {amount} {from_cur} в {dist_currency}")
        res = convert_currency(amount, from_cur, dist_currency)
        # По идее надо округлять до 2 цифр после запятой, но с финансовой точки зрения это будет некорректно
        # result = round(convert_currency(amount, from_cur, dist_currency), 2)
        logger.info(f"Получен ответ: {res}.")

    return res
