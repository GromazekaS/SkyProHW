from src.widget import get_date, mask_account_card
from tests.test_card_account import date_test, input_data_test


def main() -> None:
    """Основная часть программы!!!"""
    for test in input_data_test:
        print(mask_account_card(test))
    for test in date_test:
        print(get_date(test))


if __name__ == "__main__":
    main()
