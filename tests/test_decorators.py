import pytest

from src.widget import get_date


def test_log(capsys):
    get_date("2024-03-11T02:26:18.671407")
    captured = capsys.readouterr()
    assert captured.out.split('\n')[1] == "get_date успешно завершена. Результат: 11.03.2024"
