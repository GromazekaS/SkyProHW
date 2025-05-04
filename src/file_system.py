import csv
# from pprint import pprint

import pandas as pd

from src.logger import logger_setup

logger = logger_setup("file_system")


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
            print(type(csv_data))
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


# data = get_transactions_from_csv_file('../data/transactions.csv', ';')
# pprint(data[5])
# data = get_transactions_from_excel_file('../data/transactions_excel.xlsx')
# pprint(data[25])
