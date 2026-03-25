'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

# a sort solution. If the majority number appears more than half of the times,
# then the halfway point must be that majority element
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # below is O(n log n) due to sort function
        # nums.sort()
        # return nums[len(nums) // 2]
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else - 1

        return candidate


print(Solution().majorityElement([3,2,3]))

