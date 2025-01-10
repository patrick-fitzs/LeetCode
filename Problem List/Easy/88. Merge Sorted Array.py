class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Merges nums2 into nums1 as one sorted array in-place.
        """
        # Initialize pointers for nums1, nums2, and the merged position
        midx = m - 1  # Pointer for the last valid element in nums1
        nidx = n - 1  # Pointer for the last element in nums2
        right = m + n - 1  # Pointer for the last position in nums1

        # Iterate until all elements from nums2 are merged
        while nidx >= 0:
            # If there are remaining elements in nums1 and the current nums1 element is larger
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]  # Place the larger element in the correct position
                midx -= 1  # Move the nums1 pointer to the left
            else:
                nums1[right] = nums2[nidx]  # Place the nums2 element in the correct position
                nidx -= 1  # Move the nums2 pointer to the left

            right -= 1  # Move the pointer for the merged array to the left
