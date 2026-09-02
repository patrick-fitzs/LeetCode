"""
https://leetcode.com/problems/valid-anagram/

we could sort both and compare. This is O(n log n) for the sort function.
OR
we use counter for O(n)
"""
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = sorted(s)
        # t = sorted(t)
        # return s == t

        # easy method
        #counter_s = Counter(s)
        #counter_t = Counter(t)
        #return counter_s == counter_t





            # or you can do
        # edge case for character length checker
        if len(s) != len(t):
            return False

        # our counter
        charCounter = {}

        # add new letters and assign count of 1
        for letter in s:
            if letter not in charCounter:
                charCounter[letter] = 1
            # if they already exist, add 1
            else:
                charCounter[letter] += 1

        # compare t, they letter from t is in our couter, subtract
        for letter in t:
            if letter in charCounter and charCounter[letter] > 0:
                charCounter[letter] -= 1

            # if its not, return false

            else:
                return False

            # letters from t matched s, so a valid anagram
        return True


print(Solution().isAnagram("anagram", "nagaram"))


