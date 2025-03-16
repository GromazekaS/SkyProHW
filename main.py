from src.masks import get_mask_account, get_mask_card_number

CARD_NUMBER = 1234567812345678
ACC_NUMBER = 12345678901112131


def main() -> None:
    """Основная часть программы!!!"""
    print(get_mask_card_number(CARD_NUMBER))
    print(get_mask_account(ACC_NUMBER))


if __name__ == "__main__":
    main()
