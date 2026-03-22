"""
https://leetcode.com/problems/remove-element/

So we need to count occurences of k in a list called nums

so we iterate, does i == val? if not skip
               does i+1 == value? yes so counter++
               also replace current i with number that is not val, so the index the counter holds
"""
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # create index counter
        k = 0

        for i in range(len(nums)):
            # does 3!= val? yes so nums[k(0)]
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

print(Solution().removeElement([3,2,2,3], 3))