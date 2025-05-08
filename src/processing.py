import re
from collections import Counter
from src.logger import logger_setup
from tests.conftest import trans_test

from pprint import pprint

logger = logger_setup('processing')


def filter_by_state(records_to_filter: list[dict], state: str = "EXECUTED") -> list:
    """Отфильтровать список словарей по полю 'state'"""
    result = []
    logger.info(f"Сортирую транзакции {len(records_to_filter)} по статусу {state}")
    # logger.debug(f"Пример транзакции: {records_to_filter[0]}")
    for item in records_to_filter:
        if item.get("state") == state:
            result.append(item)
    logger.info(f"Осталось {len(result)} записей")
    return result


def sort_by_date(records_to_sort: list, reverse: bool = True) -> list:
    """Отсортировать записи в заданном порядке по полю 'date'"""
    result = sorted(records_to_sort, key=lambda x: x["date"], reverse=reverse)
    return result


def filter_by_pattern(pattern: str, transactions_list: list[dict]) -> list[dict]:
    """Найти и вернуть список транзакций с заданным шаблоном в описании"""
    result = []
    logger.info('Начинаем поиск по шаблону в описании транзакций')
    for transaction in transactions_list:
        if re.search(pattern=pattern, string=transaction['description'], flags=0):
            result.append(transaction)
    logger.info(f'Поиск завершен. Найдено {len(result)} записей, удовлетворяющих шаблону')
    return result


def category_counter(transaction_list: list[dict], category_list: list) -> dict:
    category = [x['description'] for x in transaction_list]
    result = Counter(category)

    if category_list:
        return {cat: result.get(cat, 0) for cat in category_list}
    return result


# pprint(filter_by_pattern("организации", trans_test))
# test = category_counter(trans_test, [])
# test = category_counter(trans_test, ['Перевод организации', 'Перевод с карты на карту'])
# print(test)
