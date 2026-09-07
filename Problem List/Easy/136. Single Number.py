from typing import List, Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if len(nums) == 1:
                return i

        counter = Counter(nums)
        print(counter)

        result = Counter(nums).most_common()[-1][0]
        print(result)

        return result



print(Solution().singleNumber(nums=[4,1,2,1,2]))