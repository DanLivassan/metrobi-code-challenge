from typing import List
from math import floor
carrotTypes = [{"kg": 5, "price": 100}, {"kg": 7, "price": 150}, {"kg": 3, "price": 70}]


def getMaxValue(carrot_types: List, capacity: int):
    """Function that returns a maximum value that one bag can hold"""
    carrot_types = sorted(carrot_types, key=lambda item: item['kg'], reverse=True)
    for i, carrot_type in enumerate(carrot_types, start=1):
        if capacity % carrot_type['kg'] == 0:
            return f"You can take {capacity / carrot_type['kg']} of carrot {i}"

    comb_carrots = []
    count = len(carrot_types)
    for i in range(count):
        l_capacity = capacity
        lis = [0] * len(carrot_types)
        for j in range(i, count):
            if carrot_types[j]['kg'] <= l_capacity:
                lis[i] = floor(l_capacity/carrot_types[j]['kg'])
                l_capacity = l_capacity % carrot_types[j]['kg']
        comb_carrots.append({"qtd": lis, "capacity_left": l_capacity})
    return sorted(comb_carrots, key=lambda item: item['capacity_left'])[0]


print(getMaxValue(carrotTypes, 37))
