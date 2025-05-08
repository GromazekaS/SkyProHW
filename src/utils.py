import csv
import json

import pandas as pd

from src.logger import logger_setup

# from pprint import pprint


logger = logger_setup("utils")


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


def get_transactions_from_csv_file(path: str, delimiter: str = ",") -> list[dict]:
    """Прочитать csv-файл по указанному пути, вернуть список транзакций"""
    # Если try не выполнится, функция вернет пустой список
    result_list = []
    try:
        # Пробуем открыть файл
        logger.info(f"Считываем файл csv {path}")
        inside_fields = ["amount", "currency_code", "currency_name"]
        with open(path, encoding="utf-8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=delimiter)
            headers = next(csv_data)
            # print(type(csv_data))
            for line in csv_data:
                transaction: dict = {"operationAmount": {"currency": {}}}
                for i in range(len(headers)):
                    if headers[i] in inside_fields:
                        if headers[i] == "amount":
                            transaction["operationAmount"][headers[i]] = line[i]
                        else:
                            transaction["operationAmount"]["currency"][headers[i].split("_")[-1]] = line[i]
                    else:
                        transaction[headers[i]] = line[i]
                result_list.append(transaction)
        logger.info(f"Считано {len(result_list)} записей")
    except FileNotFoundError:
        logger.error("Файл не найден")
    except Exception as e:
        logger.error(f"Произошла ошибка: {str(e)}")
    logger.info("Завершение обработки файла")
    return result_list


def get_transactions_from_excel_file(path: str) -> list[dict]:
    """Прочитать excel-файл по указанному пути, вернуть список транзакций"""
    # Если try не выполнится, функция вернет пустой список
    result_list = []
    try:
        # Пробуем открыть файл
        logger.info(f"Считываем файл excel {path}")
        excel_data = pd.read_excel(path, dtype=str)

        # Преобразуем считанные линейные данные в привычную структуру transaction
        inside_fields = ["amount", "currency_code", "currency_name"]
        for i in range(excel_data.shape[0]):
            transaction: dict = {"operationAmount": {"currency": {}}}
            for k in excel_data.iloc[0].keys():
                if k in inside_fields:
                    if k == "amount":
                        transaction["operationAmount"][k] = excel_data.loc[i, k]
                    else:
                        transaction["operationAmount"]["currency"][k.split("_")[-1]] = excel_data.loc[i, k]
                else:
                    transaction[k] = excel_data.loc[i, k]
            result_list.append(transaction)

        logger.info(f"Считано {len(result_list)} записей")
    except FileNotFoundError:
        logger.error("Файл не найден")
    except Exception as e:
        logger.error(f"Произошла ошибка: {str(e)}")
    logger.info("Завершение обработки файла")
    return result_list


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
