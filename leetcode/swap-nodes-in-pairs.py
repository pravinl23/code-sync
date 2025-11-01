# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        swapped = head.next
        prev = None

        while head and head.next:   
            first = head
            second = head.next
            third = second.next

            first.next = third
            second.next = first
            
            
            if prev:
                prev.next = second
            prev = first
            head = third

        return swapped