from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counterCheck = defaultdict(list)
        # Creates a dictionary where each new key automatically gets an empty list ***

        for s in strs:
            key = "".join(sorted(s))
            # Sorts the letters in each word and joins them back into a string
            # Anagrams will therefore have the same key


            counterCheck[key].append(s)
            # Adds the original word to the list associated with that key

        return list(counterCheck.values())
    # Returns all the groups of anagrams as a list


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))