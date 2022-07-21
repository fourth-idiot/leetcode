# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        forwardHead = ListNode(-1)
        forwardHead.next = head
        forwardCurrent = forwardHead
        for _ in range(1, left):
            forwardCurrent = forwardCurrent.next
        reverseHead = forwardCurrent.next
        reverseCurrent = reverseHead
        for _ in range(right - left):
            oldNext = reverseCurrent.next
            reverseCurrent.next = reverseCurrent.next.next
            oldNext.next = reverseHead
            reverseHead = oldNext
        forwardCurrent.next = reverseHead
        return forwardHead.next