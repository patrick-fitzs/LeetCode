import collections
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # s             = "aababcaab"
        # maxLetters    = 2
        # minSize       = 3
        # maxSize       = 4
        # We want a hashmap with countr of unique occurences,
        # counter gives us something like {'x':1, 'y':2, etc}, s[i:i+minSize] means i-i+3, so 3 letters long. len(s)=9-3+1=7 keeps us in bounds

        count = collections.Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))
        # return max numbered count in count if the len(set means unique chars is less or equal to 2) in this we have aab twice and (a and b are unique)
        return max([count[w] for w in count if len(set(w)) <= maxLetters] + [0])
        # + [0] prevent a crash if no valid string as if not valid it would be [] + [0] = [0] which is valid

print(Solution().maxFreq("aababcaab", 2, 3, 4))


class Solution_with_window:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # this holds our dictionary to count
        count = collections.Counter()

        for i in range(len(s) - minSize + 1):
            subString = s[i : i + minSize]

            if len(set(subString)) <= maxLetters:
                count[subString] += 1

        return max(count.values(), default=0)


print(Solution_with_window().maxFreq("aababcaab", 2, 3, 4))

        