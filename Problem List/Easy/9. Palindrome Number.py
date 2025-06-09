class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = 0
        copyx = x

        while x > 0:
            reverse = (reverse * 10) + (x % 10) # 0*10 + 121 modulo 10 = 0 + 1
            x //= 10 # 121/10 =12

        return reverse == copyx


print(Solution().isPalindrome(121))