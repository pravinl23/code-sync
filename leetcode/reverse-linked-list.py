# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # ITERATIVELY
    
        '''
        if not head:
            return head

        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        

        return prev
        '''

        # RECURSIVELY
        if not head or not head.next:
            return head

        newHead = self.reverseList(head.next)
        # reverse pointer
        # e.g 1->2 becomes 1<->2
        head.next.next = head
        # break the old link 
        # 1<->2 becomes 1<-2
        head.next = None

        return newHead