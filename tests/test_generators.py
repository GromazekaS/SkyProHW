import pytest

from src.generators import card_number_generator, filter_by_currency, transactions_description
from tests.conftest import trans_test


def test_filter_by_currency(transactions_test: list[dict]) -> None:
    generator = filter_by_currency(transactions_test)
    assert next(generator) == {
        "date": "2018-06-30T02:08:58.425572",
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "id": 939719570,
        "operationAmount": {"amount": "9824.07", "currency": {"code": "USD", "name": "USD"}},
        "state": "EXECUTED",
        "to": "Счет 11776614605963066702",
    }
    assert next(generator) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    assert next(generator, {}) == {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    assert next(generator, {}) == {}
    generator = filter_by_currency(transactions_test, "RUB")
    assert next(generator) == {
        "date": "2019-03-23T01:09:46.296404",
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "id": 873106923,
        "operationAmount": {"amount": "43318.34", "currency": {"code": "RUB", "name": "руб."}},
        "state": "EXECUTED",
        "to": "Счет 74489636417521191160",
    }
    assert next(generator) == {
        "date": "2018-09-12T21:27:25.241689",
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "id": 594226727,
        "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
        "state": "CANCELED",
        "to": "Счет 14211924144426031657",
    }
    generator = filter_by_currency(transactions_test, "EUR")
    assert next(generator, {}) == {}


def test_transaction_description(transactions_test: list[dict]) -> None:
    description = transactions_description(transactions_test)
    assert next(description) == "Перевод организации"
    assert next(description) == "Перевод со счета на счет"
    assert next(description) == "Перевод со счета на счет"
    assert next(description, {}) == "Перевод с карты на карту"
    assert next(description, {}) == "Перевод организации"
    assert next(description, "") == ""


# Вариант проверки функции через параметризацию
descriptions_test = [
    (
        trans_test,
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
        ],
    )
]


@pytest.mark.parametrize("transactions_list, expected", descriptions_test)
def test_transaction_description_param(transactions_list: list[dict], expected: list[str]) -> None:
    description = transactions_description(transactions_list)

    for i in range(5):
        assert next(description) == expected[i]


# Проверка корректности работы и правильности завершения
def test_card_number_generator() -> None:
    generator = card_number_generator(2020123456789101, 2020123456789105)
    assert next(generator) == "2020 1234 5678 9101"
    assert next(generator) == "2020 1234 5678 9102"
    assert next(generator) == "2020 1234 5678 9103"
    assert next(generator) == "2020 1234 5678 9104"
    assert next(generator) == "2020 1234 5678 9105"
    with pytest.raises(StopIteration) as exec_info:  # Проверка на вызов исключения после перебора заданных значений
        next(generator)
    assert str(exec_info.value) == ""


# Проверка вызова генератора с неправильными аргументами (неправильный порядок начала и окончания)
def test_card_number_generator_wrong_args() -> None:
    generator = card_number_generator(5, 1)
    with pytest.raises(ValueError) as exec_info:
        next(generator)
    assert str(exec_info.value) == "Wrong card number order. First card number is greater than last one"
