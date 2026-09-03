from collections import defaultdict, Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        charCounter = {} # out dict to store count of elems
        for num in nums:
            if num not in charCounter:
                charCounter[num] = 1 # start with 1 if not already there

            else:
                charCounter[num] += 1 # if already there add 1


        mostFreq = Counter(charCounter).most_common(k) # wrap in a counter, call most_common k elems

        keys = [item[0] for item in mostFreq] # iterate and grab just the keys


        return keys



print(Solution().topKFrequent(nums=[1,1,1,2,2,3], k=2))