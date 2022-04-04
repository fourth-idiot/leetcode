# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getPreKThNodeFromStart(self, head, k):
        for _ in range(k - 1): head = head.next
        return head
    
    def getPreKThNodeFromEnd(self, head, k):
        p1, p2 = head, head
        for _ in range(k + 1): p2 = p2.next
        while(p2 is not None):
            p1 = p1.next
            p2 = p2.next
        return p1
    
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        preHead = ListNode(-1)
        preHead.next = head
        preNode1 = self.getPreKThNodeFromStart(preHead, k)
        preNode2 = self.getPreKThNodeFromEnd(preHead, k)
        oldNode1 = preNode1.next
        preNode1.next = preNode2.next
        preNode2.next = oldNode1
        oldNextNode1 = preNode2.next.next
        preNode2.next.next = preNode1.next.next
        preNode1.next.next = oldNextNode1
        return preHead.next