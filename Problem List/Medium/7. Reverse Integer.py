'''
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # empty variable to hold reversed number
        rev = 0
        # brackets are evaluated in order from left to right
        if x < 0:
            rev = int(str(x)[1:][::-1]) * -1
        else:
            rev = int(str(x)[::-1])

        # if rev > 2**31 - 1 or rev < -2**31 :
        #     return 0

        return rev

print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
