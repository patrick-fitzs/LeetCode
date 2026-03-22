"""
https://leetcode.com/problems/valid-parentheses/description/
Input: s = "()[]{}"
we run through the iterations ,
check is '(' in things? YES -> push to stack
check is ')' in things? NO -> go to else:
            -> if not stack (is stack empty) or things[stack.pop()] !=ch (do they match?)
            if they stack is not empty and pop matched, next iteration

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



