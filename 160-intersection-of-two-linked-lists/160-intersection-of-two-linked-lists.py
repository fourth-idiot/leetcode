# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1 = headA
        len1 = 0
        while(p1 is not None):
            len1 += 1
            p1 = p1.next
        p2 = headB
        len2 = 0
        while(p2 is not None):
            len2 += 1
            p2 = p2.next
        p1 = headA
        p2 = headB
        if(len1 > len2):
            for _ in range(len1 - len2):
                p1 = p1.next
        elif(len2 > len1):
            for _ in range(len2 - len1):
                p2 = p2.next
        while(p1 != p2):
            p1 = p1.next
            p2 = p2.next
        return p1