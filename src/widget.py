from src.decorators import log, timing
from src.logger import logger_setup
from src.masks import get_mask_account, get_mask_card_number

logger = logger_setup("widget")


# @log("log_widget.txt")
# @timing
def mask_account_card(data: str) -> str:
    """Завернуть номер счета или карты в маску"""
    mask = ""
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


# @log(None)
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
