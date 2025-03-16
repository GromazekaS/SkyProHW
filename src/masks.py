def get_mask_card_number(card_number: int) -> str:
    """Вернуть номер карты маской"""
    temp = str(card_number)
    return f"{temp[:4]} {temp[4:6]}** **** {temp[11:15]}"


def get_mask_account(acc_number: int) -> str:
    """Вернуть номер аккаунта маской"""
    temp = str(acc_number)
    return f"**{temp[-4:]}"