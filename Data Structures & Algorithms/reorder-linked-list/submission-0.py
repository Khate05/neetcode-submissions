class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1, find the middle with fast and slow pointers
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2, reverse the second half and cut the link
        prev, cur = None, slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev, cur = cur, nxt

        # Step 3, merge the two halves alternately
        front, back = head, prev
        while back:
            tmp1, tmp2 = front.next, back.next
            front.next = back
            back.next = tmp1
            front, back = tmp1, tmp2