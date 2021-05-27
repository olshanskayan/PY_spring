"""
This module implements some functions based on linear search algo
"""
from typing import Sequence

my_array = [44, 20, 11, 31]

def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_index = 0
    min_value = my_array[min_index]

    for index, value in enumerate(my_array):
        if value < min_value:
            min_value = value



    print(min_value)
    return -1

if __name__ == '__main__':
    min_search(my_array)
