from time import time
from functools import wraps
from typing import Callable, Any


def timing(function: Callable) -> Callable:
    """Декоратор для определения времени выполнения функций"""
    @wraps(function)
    def time_wrapper(*args, **kwargs):
        start_timer = time()
        result = function(*args, **kwargs)  # Вызов исходной функции
        stop_timer = time()
        print(f"Время выполнения функции: {function.__name__}", stop_timer - start_timer)
        return result
    return time_wrapper


def log(filename: str | None = None) -> Callable:
    """Декоратор для логирования выполнения функций"""
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            try:
                result = func(*args, **kwargs)
                success_message = f"{func.__name__} успешно завершена. Результат: {result}\n"
            except Exception as e:
                error_message = f"{func.__name__} прервана. Ошибка: {type(e).__name__}. Аргументы вызова: args: {args}, kwargs: {kwargs}\n"
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(error_message)
                else:
                    print(error_message.strip())
                raise e
            else:
                if filename:
                    with open(filename, 'a', encoding='utf-8') as f:
                        f.write(success_message)
                else:
                    print(success_message.strip())
                return result

        return wrapper

    return decorator
