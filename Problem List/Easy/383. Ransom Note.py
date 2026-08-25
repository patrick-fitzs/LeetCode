"""
Given two strings ransomNote and magazine,
return true if ransomNote can be constructed by using the letters
from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

# Using a map here to store each character of magazine with char total.
# We then run through each letter in the note and if we find it in the map we subtract it
# if it's not in the map, or we've used all the chars, return False and stop program

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dictionary = {}

        for char in magazine:
            if char not in dictionary:
                dictionary[char] = 1
            else:
                dictionary[char] += 1

        for char in ransomNote:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                return False

        return True

print(Solution().canConstruct('aa', 'aab'))