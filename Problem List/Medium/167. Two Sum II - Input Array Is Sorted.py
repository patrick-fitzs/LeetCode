from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) -1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1] # indexed +1 in the question

            elif current_sum < target:
                left += 1

            else:
                right -= 1

print(Solution().twoSum([2, 7, 11, 15], 9))