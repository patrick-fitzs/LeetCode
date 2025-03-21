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
        mapz = {}

        for char in magazine:
            mapz[char] = 1 + mapz.get(char, 0)

        for i in ransomNote:
            if i not in mapz or mapz[i] <= 0:
                return False
            mapz[i] -= 1

        return True

