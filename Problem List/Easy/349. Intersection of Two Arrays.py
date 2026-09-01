from typing import List


'''

Return the intersection of 2 arrays. This just means the common nums between them
Literally the intersection of a set

'''

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 = set(nums1)
        # result = []
        #
        #
        # for i in range(len(nums2)):
        #     if nums2[i] in nums1 and nums2[i] not in result:
        #         result.append(nums2[i])
        #
        # return result

        set1 = set(nums1) # get rid of dupes
        result = []

        for num in nums2:
            if num in set1:
                result.append(num)
                set1.remove(num)


        return result



print(Solution().intersection(nums1=[1,2,2,1], nums2=[2,2]))