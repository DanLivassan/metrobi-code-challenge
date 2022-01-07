from typing import List


def find_duplicate(array: List) -> List:
    """Q1: Function that finds duplicated items in any given array"""
    result = []
    for item in array:
        count = 0
        for i, value in enumerate(array):
            if item == array[i]:
                count += 1
        if count > 1 and item not in result:
            result.append(item)
    return result
# print(find_duplicate([1,2,3,3,3,4,5,5]))




