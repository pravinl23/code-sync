# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        curr = head
        prev = None
        while curr and curr.next:
            if curr.next.val == curr.val:
                a = curr.val
                while curr and curr.val == a:
                    curr = curr.next
                if not prev:
                    head = curr
                else:
                    prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return head