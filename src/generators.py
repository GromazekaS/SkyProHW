import typing


def filter_by_currency(transactions: list[dict], currency_code: str = "USD") -> typing.Generator[dict]:
    return (x for x in transactions if x['operationAmount']['currency']['code'] == currency_code)


def transactions_description(transactions: list[dict]) -> typing.Generator[str]:
    return (x['description'] for x in transactions)


def card_number_generator(first: int, last: int) -> typing.Generator[str]:
    if first > last:
        raise ValueError("Wrong card number order. First card number is greater than last one")
    for n in range(first, last+1):
        card_number = str(n)
        temp = "0"*(16 - len(card_number)) + card_number
        yield temp[:4:] + " " + temp[4:8:] + " " + temp[8:12:] + " " + temp[-4::]


if __name__ == "__main__":
    pass
