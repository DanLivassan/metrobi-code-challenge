from typing import List
carrotTypes = [{"kg": 5, "price": 100}, {"kg": 7, "price": 150}, {"kg": 3, "price": 70}]


def getMaxValue(carrot_types: List, capacity: int):
    """Function that returns a maximum value that one bag can hold"""
    
    ratios = [carrot_type['price']/carrot_type['kg'] for carrot_type in carrot_types]
    carrot_types = [{"price": carrot_type["price"], "kg":carrot_type["kg"], "ratio":ratios[i]} for i,carrot_type in enumerate(carrot_types)]
    carrot_types = sorted(carrot_types, key=lambda item: item['ratio'])
    min_weight = min([carrot_type['kg'] for carrot_type in carrot_types])
    totals = {
        "bag_capacity":capacity,
        "total_in_kg":0,
        "money_spent":0,
        "left_capacity":0
    }
    while capacity>=min_weight:
        for carrot_type in carrot_types:

            if capacity/carrot_type['kg']>=1:
                capacity -= carrot_type['kg']
                totals["left_capacity"]=capacity
                totals["money_spent"]+=carrot_type["price"]
                totals["total_in_kg"]+=carrot_type["kg"]
                continue
    return totals


totals = getMaxValue(carrotTypes, 67)
print(f"You can get {totals['total_in_kg']}\nWill spent {totals['money_spent']}\nAnd left {totals['left_capacity']}kg of capacity in the bag (bag have {totals['bag_capacity']}kg of capacity)")
