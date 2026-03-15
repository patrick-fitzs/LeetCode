"""
https://leetcode.com/problems/maximum-performance-of-a-team/description/
"""

import heapq

def maxTeamPerformance(n, speed, efficiency, k):
    teams = list(zip(efficiency, speed))
    teams.sort(reverse=True)

    heap = []
    speed_sum = 0
    best = 0

    for e, s in teams:
        heapq.heappush(heap, s)
        speed_sum += s

        if len(heap) > k:
            speed_sum -= heapq.heappop(heap)

        best = max(best, speed_sum * e)

    return best % (10**9 + 7)




n = 6
speed = [2, 10, 3, 1, 5, 8]
efficiency = [5, 4, 3, 9, 7, 2]
k = 2

print(maxTeamPerformance(n, speed, efficiency, k))
