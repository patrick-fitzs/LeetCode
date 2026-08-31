from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        num_set = set(nums)
        print(num_set)

        result = [] # empty list to add missing numbers

        for i in range(1, len(nums)+1): # loop over 1, 2, 3, 4, 5, 6, 7, 8
            if i not in num_set: # if a num from 1-8 is not in set
                result.append(i) # add to set, this is out missing numbers

        return result

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))