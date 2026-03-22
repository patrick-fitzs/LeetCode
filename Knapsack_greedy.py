"""
Random generated list of items and their weights to test knapsack optimisation problems on.

first we'll try a brute force approach
then greedy,

we will also check time taken
"""

import time
from itertools import combinations

items = [
    {"weight": 3,  "value": 25},
    {"weight": 7,  "value": 42},
    {"weight": 12, "value": 60},
    {"weight": 5,  "value": 32},
    {"weight": 9,  "value": 50},
    {"weight": 4,  "value": 28},
    {"weight": 15, "value": 75},
    {"weight": 6,  "value": 38},
    {"weight": 11, "value": 58},
    {"weight": 14, "value": 72},
    {"weight": 2,  "value": 18},
    {"weight": 10, "value": 55},
    {"weight": 13, "value": 68},
    {"weight": 1,  "value": 10},
    {"weight": 23, "value": 125},
    {"weight": 25, "value": 140},
    {"weight": 28, "value": 160},
    {"weight": 30, "value": 175},
    {"weight": 27, "value": 155},
    {"weight": 29, "value": 170}
]

capacity = 60


## bruteforce approach
## this is O(2^n) - we have 2 choices and each time we add, doubles our runtime
## 2== 4 subsets, 4 == 16, 10 = 1024 etc

def knapsack_brute_force(items, capacity ):
    n = len(items)
    best_value = 0
    best_combination = None

    for r in range(n+1):
        for combination in combinations(items, r):
            total_weight = sum(item['weight'] for item in combination)
            total_value = sum(item['value'] for item in combination)
            if total_weight <= capacity and total_value > best_value:
                best_value = total_value
                best_combination = combination
                used_capacity = total_weight

    return best_value, best_combination, used_capacity


print(knapsack_brute_force(items, capacity))


## a greedy approach
## runs in O(n log n)
## because we sorted the list, this is then O(n log n)

def greedy_knapsack(items, capacity):
    items_sorted = sorted(items, key=lambda x: x['value'] / x['weight'], reverse=True)
    total_weight = 0
    total_value = 0
    chosen_items = []

    # this is O(n)
    for item in items_sorted:
        if total_weight + item['weight'] <= capacity:
            chosen_items.append(item)
            total_weight += item['weight']
            total_value += item['value']

    return total_value, chosen_items, total_weight

print(greedy_knapsack(items, capacity))

