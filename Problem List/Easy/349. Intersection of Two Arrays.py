from typing import List


'''

Return the intersection of 2 arrays. This just means the common nums between them
Literally the intersection of a set

'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1) # get rid of dupes

        result = [] # store results here to return

        for num in nums2:
            if num in s1:
                result.append(num)
                s1.remove(num)

        return result



print(Solution().intersection(nums1=[1,2,2,1], nums2=[2,2]))