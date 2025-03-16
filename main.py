from src.widget import mask_account_card, get_date
from tests.test_card_account import input_data_test, date_test


def main() -> None:
    """Основная часть программы!!!"""
    for test in input_data_test:
        print(mask_account_card(test))
    for test in date_test:
        print(get_date(test))


if __name__ == "__main__":
    main()
