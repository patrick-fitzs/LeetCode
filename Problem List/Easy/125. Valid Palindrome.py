import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', "", s).lower()
        return s == s[::-1]


#
# Straight forward approach using re library and a method sub which removes the following characters.
# lastly we use.lower and return s vs s in reverse for a true or false
print(Solution().isPalindrome("abba"))
print(Solution().isPalindrome("Defff"))

# below is a slider method #
# def isPalindrome(self, s: str) -> bool:
#     s = ''.join(c.lower() for c in s if c.isalnum())
#         left = 0
#         right = len(s) - 1
#
#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -=1
#         return True
