'''
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n%2==1:
            return float(merged[n//2])
        else:
            return (merged[n//2 - 1] + merged[n//2]) / 2.0

print(Solution().findMedianSortedArrays([1,2], [3,4]))

"""
We sort the array, and then simply return the index where (half the length of the array) 
if even and  if odd --> add both and divide to get middle index
"""