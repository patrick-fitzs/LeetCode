"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in
the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.

Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.



Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        n = len(nums) # len of list
        pointer_index = 0 # initialise a pointer index

        for i in range(1,n): # from 1 to n
            if nums[i] != nums[pointer_index]: # if 'i' is not equal to the pointer (which is behind)
                pointer_index += 1 # increment pointer
                nums[pointer_index] = nums[i] # update index

        return pointer_index + 1

nums = [1, 1, 2]
print(Solution().removeDuplicates(nums)) # print length of unique elements
length = Solution().removeDuplicates(nums)
print(nums[:length]) # prints the new list of unique elements
