from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    # middle = len(arr) // 2
    # lb = 0 # правая граница
    # rb = len(arr) // 2 # правая граница
    # while True:
    #     if elem == arr[middle]:
    #         print(elem, arr)
    #         return middle
    #
    #     if middle == 0 or middle == len(arr) - 1:
    #         returb -1

    lb = 0  # левая граница
    rb = len(arr) - 1  # правая граница
    middle = (lb + rb) // 2
    while True:
        if elem == arr[middle]:
            if arr[middle - 1] != elem:
                return middle
            else:
                middle -= 1
        if middle == 0 or middle == len(arr) - 1:
            return None
        elif elem < arr[middle]:
            rb = middle
            middle = (lb + rb) // 2
        elif elem > arr[middle]:
            lb = middle + 1
            middle = (lb + rb) // 2
