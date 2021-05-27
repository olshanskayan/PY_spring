"""
Taylor series
"""
from typing import Union
from math import factorial

DELTA = 0.0001


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """

def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    def _get_item(n: int) -> float:
        """
        Функция для получение следующего числа из бесконечного ряда Тейлора для sin(x)
        :param n: порядковый номер элемента из ряда
        :return:  элемент из бесконечного ряда Тейлора для sin(x)
        """
        if not n >= 1:
            raise ValueError

        if not isinstance(n, int):
            raise TypeError

        return ((-1) ** (n + 1)) * (x ** (2*n-1)) / factorial(2*n - 1)

    print(x)
    return 0


    print(x)
    return 0
