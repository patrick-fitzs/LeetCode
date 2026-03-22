"""
https://leetcode.com/problems/valid-parentheses/description/


"""

class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        stack = []
        things = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for chars in s:
            if chars in things:
                stack.append(chars)
            else:
                if not stack or things[stack.pop()] != chars:
                    return False

        return not stack


print(Solution().isValid("()"))
print(Solution().isValid("()(){}[]"))
print(Solution().isValid("({)()"))



