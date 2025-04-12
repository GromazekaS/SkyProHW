import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_account() -> None:
    assert get_mask_account(35383033474447895560) == "**5560"


def test_mask_account_not20() -> None:
    with pytest.raises(ValueError) as exec_info:
        get_mask_account(12)
    assert str(exec_info.value) == "Wrong account number length"


def test_mask_card() -> None:
    assert get_mask_card_number(7158300734726758) == "7158 30** **** 6758"


def test_mask_card_not16() -> None:
    with pytest.raises(ValueError) as exec_info:
        get_mask_card_number(12)
    assert str(exec_info.value) == "Wrong card number length"
