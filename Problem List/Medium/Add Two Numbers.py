# Definition for singly-linked list.
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        # Pointer for result list and carry var to hold sums greater than 0
        curr, carry = dummy, 0
        # Go until all digits are processed and any carrys are delt with
        while l1 or l2 or carry:
            # get current node from l1. No node means 0
            digit1 = l1.val if l1 else 0
            # same for l2
            digit2 = l2.val if l2 else 0

            # calculate sum from both digits and carry
            total = digit1 + digit2 + carry
            # update carry if greater than 10, e.g. 11 = 1 for carry
            carry = total // 10
            # current digit we'll store in results list
            digit = total % 10

            # create a new node with digit and appends to curr which is out results list
            curr.next = ListNode(digit)
            # move curent to next node
            curr = curr.next
            # lastly move to the next nodes if they exist, or None which gets ou tof while loop
            l1, l2 = (l1.next if l1 else None), (l2.next if l2 else None)

        # return node, skip dummy (only a dummy node)
        return dummy.next
