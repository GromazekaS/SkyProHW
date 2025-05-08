from src.decorators import log, timing
from src.logger import logger_setup
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_pattern

logger = logger_setup("widget")


# @log("log_widget.txt")
# @timing
def mask_account_card(data: str) -> str:
    """Завернуть номер счета или карты в маску"""
#    mask = ""
    temp = data.split()
    if temp[0] == "Счет":
        logger.info("Маскирую номер счета")
        try:
            mask = get_mask_account(int(temp[-1]))
        except Exception as ex:
            logger.error(f"Возникла ошибка {ex} при попытке маскировать счет {data}")
            return ""
    else:
        logger.info(f"Маскирую номер карты {temp[:-1]}")
        try:
            mask = get_mask_card_number(int(temp[-1]))
        except Exception as ex:
            logger.error(f"Возникла ошибка {ex} при попытке маскировать счет {data}")
            return ""
    result = data[: len(data) - len(temp[-1])] + mask
    logger.info("Маскирование успешно завершено")
    return result


@log(None)
# @timing
def get_date(date: str) -> str:
    """Вернуть дату в формате ДД.ММ.ГГГГ"""
    result = ""
    try:
        logger.info("Преобразуем формат даты")
        temp = date.split("T")[0].split("-")
        result = ""
        for item in temp[::-1]:
            result += item + "."
        result = result[:-1]
    except Exception as ex:
        logger.error(f"Возникла ошибка {ex} при преобразовании строки {date} в дату")
    return result


def check_validity_state(state: str) -> str | bool:
    """Проверить ввод пользователя"""
    # print(f"Проверяем {state}, {ord(state[0])}")
    if state.upper() in ['E', 'EXECUTED']: return 'EXECUTED'
    if state.upper() in ['C', 'CANCELED']: return 'CANCELED'
    if state.upper() in ['P', 'PENDING']: return 'PENDING'
    return False


def display_transactions(transactions_list: list[dict], category : str) -> None:
    """Отобразить банковские операции из выборки"""
    if category:
        print(f"Вывод транзакций по категории {category}\n")
        transactions_list = filter_by_pattern(category, transactions_list)
    else:
        print("Вывод транзакций по всем категориям: \n")
    print('Всего банковских операций в выборке: ', len(transactions_list), '\n')
    for item in transactions_list:
        print(f"{get_date(item['date'])} {item['description']}")
        if category == 'Открытие вклада':
            print(f"{mask_account_card(item['to'])}")
        else:
            print(f"{mask_account_card(item['from'])} - > {mask_account_card(item['to'])}")
        value = item['operationAmount']
        print(f"Сумма: {value['amount']} {value['currency']['name']}\n")
