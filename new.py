"""Вычисляет квадратный корень числа
и печатает его на экран.
"""
from math import sqrt


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Печатает квадратный корень числа."""
    if your_number <= 0:
        return None
    root = calculate_square_root(your_number)
    print(f"Мы вычислили квадратный корень из введённого вами числа. "
          f"Это будет: {root:.3f}")


message: str = ('Добро пожаловать в самую лучшую программу для '
                'вычисления квадратного корня из заданного числа')
print(message)
calc(25.5)
