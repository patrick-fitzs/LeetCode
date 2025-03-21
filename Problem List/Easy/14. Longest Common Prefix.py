"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
'''
start with a var to store the result,
then sort the list of strings,
then grab first and last words, (if these dont have in common letters than no words do)
iterate over letters, if not equal return result,
else add to result.
'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ""

        strings = sorted(strs)
        first = strings[0]
        last = strings[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return result
            else:
                result += first[i]

        return result

print(Solution().longestCommonPrefix(["flower","flow","flight"]))