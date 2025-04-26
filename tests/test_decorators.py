import pytest

from src.widget import get_date
from src.decorators import log


def test_log(capsys):
    get_date("2024-03-11T02:26:18.671407")
    captured = capsys.readouterr()
    assert captured.out.split('\n')[1] == "get_date успешно завершена. Результат: 11.03.2024"


def test_console_logging(capsys):
    @log()
    def test_func(x):
        return x * 2

    test_func(5)
    captured = capsys.readouterr()
    assert 'test_func успешно завершена. Результат: 10' in captured.out


def test_file_logging():
    log_file = "test.log"

    @log(log_file)
    def test_func():
        return 42

    test_func()

    with open(log_file, 'r', encoding="utf-8") as f:
        content = f.read()
        assert 'test_func успешно завершена. Результат: 42' in content


def test_error_logging(capsys):
    @log()
    def error_func(a, b):
        raise ValueError("Oops")

    with pytest.raises(ValueError):
        error_func(1, b=2)

    captured = capsys.readouterr()
    assert "error_func прервана." in captured.out
    assert "Аргументы вызова: args: (1,), kwargs: {'b': 2}" in captured.out
    assert "Ошибка: ValueError" in captured.out
