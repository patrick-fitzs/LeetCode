from typing import List
from collections import defaultdict, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == k:
            return nums # gives us O(1) / straight return

        numCounter = {} # our dict to hold counts

        for num in nums:
            if num not in numCounter:
                numCounter[num] = 1 # create the num count if not in our dict

            else:
                numCounter[num] += 1 # increment by 1 if it is


        mostFrequent = Counter(numCounter).most_common(k) # a Counter function to grab most freq elements

        key = [item[0] for item in mostFrequent] # iterate and grab keys


        return key









print(Solution().topKFrequent(nums=[1,1,1,2,2,3], k = 2))
