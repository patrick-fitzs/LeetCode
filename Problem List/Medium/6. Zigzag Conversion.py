'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # base case
        if numRows == 1 or numRows >= len(s):
            return s
        # index and step (or level of row)
        index, step = 0, 1

        # create list of rows
        rows = [[] for _ in range(numRows)]

        # iterate over s
        for char in s:
            rows[index].append(char)
            if index == 0:
                d = 1
            # if we reach the end of the numRows
            elif index == numRows - 1:
                d = -1
            # add or subtract
            index += d

        for i in range(numRows):
            # join characters together into lists
            rows[i] = ''.join(rows[i])

        return ''.join(rows)

x = Solution().convert("PAYPALISHIRING", 4)
if x == "PINALSIGYAHRPI":
    print(True)