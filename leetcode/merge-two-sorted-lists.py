# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode(0)
        curr = head
        while list1 and list2:
            while list1 and list2 and list1.val < list2.val:
                print(list1)
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                curr.next = None
            while list1 and list2 and list2.val <= list1.val:
                print(list2)
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                curr.next = None

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        head = head.next

        return head