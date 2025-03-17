'''
2594. Minimum Time to Repair Cars
Medium
Topics
Companies
Hint
You are given an integer array ranks representing the ranks of some mechanics. ranks i is the rank of the ith mechanic.
A mechanic with a rank r can repair n cars in r * n2 minutes.

You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.

Return the minimum time taken to repair all the cars.

Note: All the mechanics can repair the cars simultaneously.



Example 1:

Input: ranks = [4,2,3,1], cars = 10
Output: 16
Explanation:
- The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
- The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
- The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
- The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
'''


class Solution:
    def repairCars(self, ranks: list[int], cars: int) -> int:
        # min time possible is 1
        # max time is slowest mechanic(highest rank) repair all the cars
        low, high = 1, cars * cars * ranks[0]

        # binary search to find min time
        while low < high:
            mid = (low + high) // 2
            cars_repaired = sum(int((mid/rank) ** 0.5) for rank in ranks)

            # if th etotal cars repaired is less than required, increase the time
            if cars_repaired < cars:
                low = mid + 1
            else:
                high = mid

        return low


print(Solution().repairCars([4,2,3,1], 10))