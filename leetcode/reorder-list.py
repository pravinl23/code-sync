class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        # Step 1: find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: split and reverse second half
        second = slow.next
        slow.next = None
        prev = None
        curr = second
        while curr:
            tempnext = curr.next
            curr.next = prev
            prev = curr
            curr = tempnext

        # Step 3: merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2