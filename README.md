# Учебный проект для изучения основ программирования на Python и освоения инструментов разработки
Проект по учету работы с банковскими картами

## Функционал проекта:
1. Функции get_mask_account() и get_mask_card_number() для маскирования номера счет и номера банковской карты (masks.py).
2. Отображение (widget.py):

   2.1 Функция mask_account_card() маскирующая входную информацию, использует функции из п.1.
   2.2 Функция get_date() для преобразования даты в формате timestamp в более популярный "дата время".
3. Функции filter_by_state() и sort_by_date() для сортировки записей по состоянию и дате соответственно (processing.py)
4. Созданы тесты для написанных функций
5. Функция filter_by_currency() для сортировки списка транзакций по коду валюты.
6. Функция transactions_description() для последовательного перебора описания всех транзакций из списка.
7. Функция card_number_generator() для создания набора номеров кард из заданного диапазона
8. Декоратор @log для фиксирования выполнения и вводных данных при возникновении ошибки
9. Декоратор @timing для отслеживания времени выполнения функций
10. Модуль external_api.py. Реализована функция convert_currency для конвертации валют по текущему курсу через запрос с внешного сайта по api
11. Модуль utils.py:

    11.1 Функция get_from_file - считывание данных о транзакциях из json-файла

    11.2 Функция calculate_transaction_amount - расчет суммы операции в другой валюте
12. Модуль file_system.py:

    12.1 Функция get_transactions_from_csv_file- считывание данных о транзакциях из csv-файла

    12.2 Функция get_transactions_from_excel_file- считывание данных о транзакциях из excel-файла

## Тестирование проекта:
### Тестирование masks.py
1. test_mask_account() - корректность работы функциии
2. test_mask_account_not20() - корректность реакции на неправильную длину
3. test_mask_card() - корректность работы функциии
4. test_mask_card_not16() - - корректность реакции на неправильную длину

### Тестирование widget.py
1. test_mask_account_card() - тест с параметризацией, корректность работы функциии
2. test_get_date() - тест с параметризацией, корректность работы функциии

### Тестирование processing.py
Задана фикстура processing_test
1. test_filter_by_state(processing_test) - корректность работы функциии с аргументами по умолчанию
2. test_filter_by_state_canceled(processing_test) - корректность работы функциии с заданными аргументами
3. test_sort_by_date(processing_test) - корректность работы функциии с аргументами по умолчанию (по убыванию даты)
4. test_sort_by_date_reverse(processing_test) - корректность работы функциии с заданными аргументами (по возрастанию даты)

### Тестирование generators.py
Задана фикстура transaction_test
1. test_filter_by_currency(transactions_test) - корректность работы, правильность завершение работы итератора
2. test_transaction_description(transactions_test) - корректность работы, правильность завершение работы итератора
3. test_card_number_generator() - корректность работы в заданном диапазоне
4. test_card_number_generator_wrong_args() - корректность ошибки при неправильном порядке аргументов

### Тестирование decorators.py
1. test_log - проверка вывода в консоль успешного результата функционирования get_data
2. test_console_logging - проверка вывода успешного выполнения в консоль
3. test_file_logging - проверка вывода в лога в заданный файл
4. test_error_logging - проверка неудачного выполнения функции, с выводом аргументов

### Тестирование external_api.py
1. test_convert_currency - проверка работы функции без обращения к внешнему сайту. Используется @patch для имитации обращения по api, применен Mock для подмены api-ключа, чтобы не светить его в тесте

### Тестирование utils.py
1. test_get_transactions_from_valid_file - проверка корректной работы
2. test_get_transactions_file_not_found - проверка отклика на отсутствующий файл
3. test_get_transactions_invalid_json - проверка отклика на неправильный json
4. test_get_transactions_invalid_structure - проверка отклика на неправильную структуру json-файла
5. test_calculate_transaction_amount - проверка корректной работы

### Тестирование file_system.py
1. test_get_transactions_from_csv_file_success - проверка корректной работы
2. test_get_transactions_from_csv_file_file_not_found - проверка отклика на отсутствующий файл
3. test_get_transactions_from_excel_file_success - проверка корректной работы
4. test_get_transactions_from_excel_file_file_not_found - проверка отклика на отсутствующий файл
5. test_get_transactions_from_excel_file_generic_error - проверка отклика на неожиданную ошибку

## Логирование:
1. widget.py
2. utils.py
3. masks.py
4. file_system.py

