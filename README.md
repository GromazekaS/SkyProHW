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