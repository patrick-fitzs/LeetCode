"""
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

This is very similar to 1383 problem.
We paid the relevant attributes, sort by the controlling metric, in this case ration/efficiency
then we iterate which maintaining the optimal k candidates using a heap for efficiency
"""


import heapq
def mincostToHireWorkers(quality, wage, k):
    # quality =     [10, 20, 5]
    # wage =        [70, 50, 30]
    # k = max workers          2

    # this is the ratio of wage/quality
    workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
    # so we have =       [70/10, 10][50/20, 20][30/5, 5]
    # so this equals =   [7, 10]    [2.5, 20]  [6, 5]
    # sorted =          [(2.5, 20),(6, 5),(7, 10)]

    quality_sum = 0  # return the sum of qualities
    heap = []  # to store the qualities
    best = float('inf')  # because we want the smallest

    for ratio, q in workers:
        heapq.heappush(heap, -q)
        quality_sum += q

        if len(heap) > k: quality_sum += heapq.heappop(heap)

        if len(heap) == k: best = min(best, quality_sum * ratio)

    return best


quality = [10, 20, 5]
wage = [70, 50, 30]
k = 2
print(mincostToHireWorkers(quality, wage, k))

quality2 = [3,1,10,10,1]
wage2 = [4,8,2,2,7]
k2 = 3

print(mincostToHireWorkers(quality2, wage2, k2))