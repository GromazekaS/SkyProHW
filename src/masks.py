import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Вернуть номер карты маской"""
    logger.info("Маскирую номер карты")
    temp = str(card_number)
    if len(temp) == 16:
        logger.info("Маскирование номера карты выполнено")
        return f"{temp[:4]} {temp[4:6]}** **** {temp[12:16]}"
    else:
        logger.error("Неправильная длина номера карты")
        raise ValueError("Wrong card number length")


def get_mask_account(acc_number: int) -> str:
    """Вернуть номер аккаунта маской"""
    logger.info("Маскирую номер карты")
    temp = str(acc_number)
    if len(temp) == 20:
        logger.info("Маскирование номера карты выполнено")
        return f"**{temp[-4:]}"
    else:
        logger.error("Неправильная длина номера счета")
        raise ValueError("Wrong account number length")
