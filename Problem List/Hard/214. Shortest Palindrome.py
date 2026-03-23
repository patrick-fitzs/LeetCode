"""
https://leetcode.com/problems/shortest-palindrome/description/


"""

class Solution:
    def shortestPalindrome(self, s:str) -> str:
        # store the reverse of the string to compare bit by bit
        r = s[::-1]

        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

#s = "dedcba"
#r = "abcded"
# so we check does s start with abcded? no
# then onto i=1 , does s start with bcded? no becasue it starts with d
# i=2, does s start with cded? no
# i = 3, does s start with d? yes!
# return r up to i, so [abc] + s which is dedcba so abcdedcba

print(Solution().shortestPalindrome("dedcba"))