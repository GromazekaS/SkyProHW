import json
import logging

from src.external_api import convert_currency

# from pprint import pprint


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/log_utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_from_file(path: str) -> list[dict]:
    """Прочитать json-файл по указанному пути, вернуть список транзакций"""
    # Если try не выполнится, функция вернет пустой список
    data = []
    try:
        # Пробуем открыть файл
        logger.info(f"Считываем файл {path}")
        with open(path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

        # Проверка структуры данных
        logger.info("Проверяем структуру считанных данных в файле")
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            logger.info("Успешно загружено {} записей".format(len(data)))
        else:
            logger.warning("Файл имеет некорректную структуру")
            data = []

    except FileNotFoundError:
        logger.error("Файл не найден")
    except json.JSONDecodeError:
        logger.error("Ошибка разбора JSON")
    except Exception as e:
        logger.error(f"Произошла ошибка: {str(e)}")
    logger.info("Завершение обработки файла")
    return data


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
