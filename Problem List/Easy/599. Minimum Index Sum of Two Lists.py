import collections
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        index_map = {word: i for i,word in enumerate(list1)}
        #print(index_map)
        result = []
        minimum_sum = float("inf")

        #print(list2)
        for j, word in enumerate(list2):
            if word in index_map:
                index_sum = j + index_map[word]
                #print(index_sum)
                if index_sum < minimum_sum:
                    minimum_sum = index_sum
                    result = [word]
                elif index_sum == minimum_sum:
                    result.append(word)

        return result


print(Solution().findRestaurant(
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
    list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
))
