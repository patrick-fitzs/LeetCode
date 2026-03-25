"""

https://leetcode.com/problems/first-letter-to-appear-twice/description/

- Pretty easy solution, as were only seeing lowercase letters, at most we could have
 a lookup time of O(26)
A hashset would be useless here (no need to add to counter and return first > 1

"""

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = []
        for char in s:
            if char in seen:
                return char

            else:
                seen.append(char)


s = "abccbaacz"
print(Solution().repeatedCharacter(s))

