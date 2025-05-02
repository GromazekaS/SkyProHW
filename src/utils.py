import json
from pprint import pprint
from src.external_api import convert_currency


def get_transactions_from_file(path: str) -> list[dict]:
    """Прочитать json-файл по указанному пути, вернуть список транзакций"""
    # Если try не выполнится, функция вернет пустой список
    data = []
    try:
        # Пробуем открыть файл
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Проверка структуры данных
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            print("Успешно загружено {} записей".format(len(data)))
        else:
            print("Файл имеет некорректную структуру")
            data =[]

    except FileNotFoundError:
        print("Файл не найден")
    except json.JSONDecodeError:
        print("Ошибка разбора JSON")
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    return data


def calculate_transaction_amount(transaction: dict, dist_currency: str='RUB') -> float:
    """Пересчет суммы транзакции в заданной валюте"""
    pprint(transaction)
    amount = transaction["operationAmount"]["amount"]
    from_cur = transaction["operationAmount"]["currency"]["code"]
    if from_cur == dist_currency:
        res = amount
        print(f'Конвертация не требуется. {amount} {dist_currency}')
    else:
        res = convert_currency(amount, from_cur, dist_currency)
        # По идее надо округлять до 2 цифр после запятой, но с финансовой точки зрения это будет некорректно
        # result = round(convert_currency(amount, from_cur, dist_currency), 2)
        print(f'{amount} {from_cur} в {dist_currency} будет {res}, {type(res)}')

    return res
'''

def main():
    """Локальная проверка функций"""
    file = 'operations.json'
    filepath = '../data/' + file
    f = get_transactions_from_file(filepath)

    # Вызов внешней функции по конвертации валют через сайт
    result = calculate_transaction_amount(f[41])
    print(result)


if __name__ == "__main__":
    main()'''
