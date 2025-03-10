'''
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :type s: str
        :param s: a string
        :return: the longest palindrome
        """
        if not s:
            return ""

        def expands_around_center(s, left, right):
            while left >= 0 and right < len(s) and  s[left] == s[right]:
                left -=1
                right +=1
            return right - left - 1

        start, end = 0, 0

        for i in range(len(s)):
            odd = expands_around_center(s, i, i)
            even = expands_around_center(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]


print(Solution().longestPalindrome("babad"))