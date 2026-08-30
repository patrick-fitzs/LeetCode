from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        #print(num_set) # set for O(1) look up



        for i in range(len(nums) +1): # loop from  0 - n
            if i not in num_set:  # if not in our set, return it
                return i





print(Solution().missingNumber([3, 0, 1]))
#print(Solution().missingNumber([0, 1]))
#print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))