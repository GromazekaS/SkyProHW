from src.logger import logger_setup

logger = logger_setup("masks")


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
