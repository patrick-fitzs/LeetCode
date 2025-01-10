# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## pointer node to head of the list
        current = head
        ## loop through the list
        while current and current.next:
            ## if the next node has the same value as the current node
            if current.next.val == current.val:
                ## current next node is now the node after the next node
                current.next = current.next.next
            else:
                ## else move the current node to the next node
                current=current.next
        return head