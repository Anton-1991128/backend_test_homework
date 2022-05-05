from typing import Callable

def add(number:float, callback):
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие.
    """    
    return callback(number)


def adder20(number:float):
    """Добавляет к аргументу 20."""
    return number + 20


def multiplier2(number:float):
    """Умножает аргумент на 2."""
    return number * 2
    print(__annotations__)