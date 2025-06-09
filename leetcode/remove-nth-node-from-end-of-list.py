# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        forward = dummy
        behind = dummy

        # move forward pointer ahead
        for i in range(n):
            forward = forward.next

        # move both pointers until foward one reaches the end i.e none
        while forward.next is not None:
            forward = forward.next
            behind = behind.next

        # Delete the nth node from end
        behind.next = behind.next.next

        return dummy.next