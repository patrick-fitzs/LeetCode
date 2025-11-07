"""
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a ,2) + int(b ,2))[2:]

    # So we first read the binary string 11, as base 2 which is 2+1, now as an int (do the same to b and add)
    # and then return the binary but from index 2 onwards


print(Solution().addBinary('11',"1"))

