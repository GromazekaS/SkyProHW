# from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date
from tests.test_card_account import date_test, input_data_test, processing_test


def main() -> None:
    """Основная часть программы!!!"""
#    for test in input_data_test:
#        print(mask_account_card(test))
#    for test in date_test:
#        print(get_date(test))
    print(filter_by_state(processing_test))
    print(filter_by_state(processing_test, 'CANCELED'))
    print(sort_by_date(processing_test))
    print(sort_by_date(processing_test, True))


if __name__ == "__main__":
    main()
