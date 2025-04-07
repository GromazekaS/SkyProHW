from src.masks import get_mask_account, get_mask_card_number


def test_mask_account() -> None:
    assert get_mask_account(35383033474447895560) == "**5560"


def test_mask_card() -> None:
    assert get_mask_card_number(7158300734726758) == "7158 30** **** 6758"
