"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/

we have an array of integers[-4,-1,0,3,10]
        sliding window approach
        nums = [-4,-1,0,3,10]
These numbers squared are all going to be positive so we don't care
if they're positive or not to begin with.
we know the biggest is doing to be on the right , so if we

start at both ends, and slide in, replacing if left is > that right,
else: we square the right  and move to next index
"""


class Solution:
    def sortedSquares(self, nums):
        # have our array to store
        result = [0] * len(nums)
        # initialise left and right
        left = 0
        right = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            #use abs so all are positive
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] **2
                left += 1

            else:
                result[i] = nums[right] **2
                right -= 1

        return result


print(Solution().sortedSquares([-4,-1,0,3,10]))

