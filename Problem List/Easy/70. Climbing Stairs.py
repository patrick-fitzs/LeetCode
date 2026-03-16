"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        # less than 2 return that number
        if n <= 2:
            return n

        # create array of zeros, size n+1 (index 0 unused, 1..n is what we care about)
        dp = [0] * (n + 1)
        dp[1] = 1  # 1 way to reach step 1
        dp[2] = 2  # 2 ways to reach step 2

        # fill in steps 3 through n
        # each step = sum of the two steps before it (fibonacci pattern)
        for steps in range(3, n + 1):
            dp[steps] = dp[steps - 1] + dp[steps - 2]

        return dp[n]