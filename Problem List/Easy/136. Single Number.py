from typing import List, Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # edge case for just 1 num in the list, just return it.
        for i in nums:
            if len(nums) == 1:
                return i

        # make a counter of nums list
        nums = Counter(nums)
        print(nums)  # just looking at nums

        # return by order of most common
        # but access the end and return
        single_num = nums.most_common()[-1][0]
        return single_num

print(Solution().singleNumber(nums=[4,1,2,1,2]))