"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 """

'''
so we can start at the last char and count backwards.
give the last index a number.
make sure last char is not empty space.
then count this as the start point. 
and while the start is not empty and the index is greater than 0
'''
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == " ":
            end -= 1

        start = end

        while start >= 0 and s[start] != " ":
            start -= 1

        return end - start

word = "Hello World"
print(Solution().lengthOfLastWord(word))