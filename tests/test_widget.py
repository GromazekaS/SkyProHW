import pytest
from src.widget import get_date, mask_account_card
from tests.conftest import card_acc_test, date_test


@pytest.mark.parametrize("x, expected", card_acc_test)
def test_mask_account_card(x: str, expected: str) -> None:
    assert mask_account_card(x) == expected


@pytest.mark.parametrize("x, expected", date_test)
def test_get_date(x: str, expected: str) -> None:
    assert get_date(x) == expected