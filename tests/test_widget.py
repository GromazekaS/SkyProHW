import pytest
from _pytest.capture import CaptureFixture

from src.widget import check_validity_state, display_transactions, get_date, mask_account_card
from tests.conftest import card_acc_test, date_test, trans_test


@pytest.mark.parametrize("x, expected", card_acc_test)
def test_mask_account_card(x: str, expected: str) -> None:
    assert mask_account_card(x) == expected


@pytest.mark.parametrize("x, expected", date_test)
def test_get_date(x: str, expected: str) -> None:
    assert get_date(x) == expected


validate_state = [
    ("e", "EXECUTED"),
    ("E", "EXECUTED"),
    ("executed", "EXECUTED"),
    ("EXECUTED", "EXECUTED"),
    ("c", "CANCELED"),
    ("C", "CANCELED"),
    ("canceled", "CANCELED"),
    ("CANCELED", "CANCELED"),
    ("p", "PENDING"),
    ("P", "PENDING"),
    ("pending", "PENDING"),
    ("PENDING", "PENDING"),
    ("f", False),
    ("test", False),
    ("F", False),
    ("аврал", False),
]


@pytest.mark.parametrize("x, expected", validate_state)
def test_check_validity_state(x: str, expected: str):
    assert check_validity_state(x) == expected


def test_display_transactions(capsys: CaptureFixture[str]) -> None:
    display_transactions(trans_test, "Перевод организации")
    captured = capsys.readouterr()
    test = captured.out.split("\n")
    assert "Вывод транзакций по категории Перевод организации" in test
    assert "Всего банковских операций в выборке:  2 " in test
    assert "30.06.2018 Перевод организации" in test
    assert "Счет **6952 - > Счет **6702" in test
    assert "Сумма: 9824.07 USD" in test
    assert "12.09.2018 Перевод организации" in test
    assert "Visa Platinum 1246 37** **** 3588 - > Счет **1657" in test
    assert "Сумма: 67314.70 руб." in test
