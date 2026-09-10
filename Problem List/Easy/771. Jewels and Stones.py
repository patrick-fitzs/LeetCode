class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        # count = 0
        #
        # for char in jewels:
        #     if char in stones:
        #         count += stones.count(char)
        #
        #
        # return count

        matching = 0

        for i in jewels:
            if i in stones:
                matching += stones.count(i)

        return matching





print(Solution().numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
