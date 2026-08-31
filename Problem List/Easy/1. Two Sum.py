"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            comp_num = target - num

            if comp_num in seen:
                return seen[comp_num], i
            seen[num] = i
''' 
 This is what iterations look like
    0, 1, 2, 3
    2, 7, 11, 15 - this is the enum

    target = 9
    compnum = 2  (9-7, the 2nd iteration)
    {2: 0, } - added from the first iteration seen{} num which is 2 so seen{2:} = 0 so seen{2:0}
    return {0, 1}
'''
print(Solution().twoSum([2, 7, 11, 15], 9))