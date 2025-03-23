"""
This program extracts decimal numbers from a text using a generator function 
and calculates their total sum.
"""

import re
from decimal import Decimal
from typing import Callable


def generator_numbers(text: str):
    for match in re.findall(r"\b\d+\.\d{1,2}\b", text):   # Знаходимо числа в тексті у форматі через крапку, 2 знаки після крапки
        yield Decimal(match)                              # Повертаємо число як Decimal для обчислення з точністю


def sum_profit(text: str, func: Callable):
    return sum(func(text))


if __name__ == "__main__":                                # Перевіряємо лише всередині цього файлу
    text = (
        """Загальний дохід працівника складається з декількох частин:
        1000.01 як основний дохід, доповнений додатковими надходженнями
        27.45 й 324.00 доларів."""
        )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")