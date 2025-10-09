# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        lists = [l for l in lists if l]


        def mergeTwoLists(list1, list2):
            """
            :type list1: Optional[ListNode]
            :type list2: Optional[ListNode]
            :rtype: Optional[ListNode]
            """
            head = ListNode(0)
            curr = head
            while list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
                else:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next

            if list1:
                curr.next = list1
            elif list2:
                curr.next = list2

            return head.next
        if not lists:
            return None   
        if len(lists) == 1:
            return lists[0]

        def DCMerge(l):
            if len(l) == 2:
                return mergeTwoLists(l[0], l[1])
            elif len(l) == 3:
                return mergeTwoLists(l[0], mergeTwoLists(l[1], l[2]))
            else:
                middle = len(l) // 2 + 1
                return mergeTwoLists(self.mergeKLists(l[:middle]), self.mergeKLists(l[middle:]))

        return DCMerge(lists)