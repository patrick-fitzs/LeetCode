
"""
https://leetcode.com/problems/sqrtx/

so to find the square root of 9 for eg, the answer is betwene 0 and 9
so we search that space, multiplying x by x, instead of brute force 0 to 9, we
can use binary search to change from O(n) to O(log n)

e.g. 9+1=10
            left=1, right = 9//2 = 4
            mid = (1+4)//5 = 2
            2*2=4, is this 9? no

            left = mid+1 so 2+1=3
            right = 4
            mid = (3+4)//2 = 7 // 2 = 3
            3*3=9, is this 9? YES

"""


def mySqrt(x):
    if x < 2: return x

    left, right = 1, x //2

    while left <= right:
        mid = (left + right) //2
        square = mid * mid

        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid -1

    return right


print(mySqrt(9))
print(mySqrt(4))
