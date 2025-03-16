from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:
    """Завернуть номер счета или карты в маску"""
    temp = data.split()
    if temp[0] == 'Счет':
        mask = get_mask_account(int(temp[-1]))
    else:
        mask = get_mask_card_number(int(temp[-1]))
    result = data[:len(data) - len(temp[-1])] + mask
    return result

def get_date(date: str) -> str:
    """Вернуть дату в формате ДД.ММ.ГГГГ"""
    temp = date.split('T')[0].split('-')
    result = ''
    for item in temp[::-1]:
        result += item + '.'
    return result[:-1]