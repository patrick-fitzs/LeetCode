"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
"""

# Definition for a binary tree node.)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        # this starts our queue, add to back remove from front O(1) operations
        queue = deque([root])

        # keeps track
        seen_null = False

        while queue:
            node = queue.popleft() # get rid of left

            if node is None:
                seen_null = True

            else:
                if seen_null:
                    return False

                queue.append(node.left)
                queue.append(node.right)

        return True
# root = [1,2,3,4,5,6]
# Start with 1 in the queue
# remove 1, queue becomes []
# add 1's children: 2 and 3
# queue = [2, 3]

# remove 2
# add 2's children: 4 and 5
# queue = [3, 4, 5]

# remove 3
# add 3's children: 6 and None
# queue = [4, 5, 6, None]

# remove 4
# add 4's children: None and None
# queue = [5, 6, None, None, None]

# seen_null stays false throughout, if we see a none, we set it to true,
# keep running
# but if we ome across another number, we then skip if node is none,
# because it's a thing again and straight into the else and return False