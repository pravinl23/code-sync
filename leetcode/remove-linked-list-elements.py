# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next:
            if curr.next.val == val:
                #extend right pointer
                curr.next = curr.next.next
            else:
                #make left pointer the right
                curr = curr.next

        return dummy.next