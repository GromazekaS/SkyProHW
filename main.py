from src.widget import get_date, mask_account_card
from time import sleep
# from src.processing import filter_by_state, sort_by_date
# from tests.conftest import processing_test  # , date_test, input_data_test


def main() -> None:
    """Основная часть программы!!!"""

    # Обертка @log (без имени файла логирования) и @timing
    get_date("2024-03-11T02:26:18.671407")

    # Обертка @log (log_widget.txt) и @timing
    mask_account_card("MasterCard 7158300734726758")

    # Проверка извлечения оригинальной функции из под двух оберток
    g = get_date
    print(g.__wrapped__.__wrapped__("2024-03-11T02:26:18.671407"))


#    for test in input_data_test:
#        print(mask_account_card(test))
#    for test in date_test:
#        print(get_date(test))
#    print(filter_by_state(processing_test))
#    print(filter_by_state(processing_test, 'CANCELED'))
#    print(sort_by_date(processing_test))
#    print(sort_by_date(processing_test, True))


if __name__ == "__main__":
    main()
