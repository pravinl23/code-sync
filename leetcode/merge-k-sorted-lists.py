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


        def mergeTwoLists(self, list1, list2):
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
        merged = lists[0]
        for i in range(len(lists)-1):
            merged = mergeTwoLists(self, merged, lists[i+1])

        return merged