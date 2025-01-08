# Given an integer array nums and an integer val,
# remove all occurrences of val in nums in-place. The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # create index counter
        index = 0
        # iterate over list
        for i in range(len(nums)):
            # if current point in list is not = to val
            if nums[i] != val:
                # first index num is now nums[i]... then second and so on
                nums[index] = nums[i]
                # increment for next loop
                index += 1
        return index