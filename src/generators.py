import typing


def filter_by_currency(transactions: list[dict], currency_code: str = "USD") -> typing.Generator[dict]:
    """Отфильтровать список транзакций по полю кода валюты"""
    return iter(x for x in transactions if x["operationAmount"]["currency"]["code"] == currency_code)


def transactions_description(transactions: list[dict]) -> typing.Generator[str]:
    """Выдавать по одному описание транзакции из всего списка"""
    gen = (x["description"] for x in transactions)
    while True:
        yield next(gen, "")


def card_number_generator(first: int, last: int) -> typing.Generator[str]:
    """Сгенерировать набор номеров карт в заданном диапазоне"""
    if first > last:
        raise ValueError("Wrong card number order. First card number is greater than last one")
    for n in range(first, last + 1):
        card_number = str(n)
        temp = "0" * (16 - len(card_number)) + card_number
        yield temp[:4:] + " " + temp[4:8:] + " " + temp[8:12:] + " " + temp[-4::]


if __name__ == "__main__":
    pass
