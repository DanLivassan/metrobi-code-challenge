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

print(find_duplicate([{"name":"danilo"}, {"name":'caio'}, {"name":'caio'}]))

class Person:

    def __init__(self, name) -> None:
        self.name = name
    def __eq__(self, __o: object) -> bool:
        return self.name==__o.name


person = Person("Danilo")
person2 = Person("Danilo")

print((person==person2))

        
print(find_duplicate_v2([1,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,51,2,3,3,3,4,5,5]))
