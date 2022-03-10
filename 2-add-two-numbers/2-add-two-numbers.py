# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Metadata
        lHead = None
        isRemainder = False
        
        # Add two linked lists till one of the lists exhaust
        while((l1 is not None) and (l2 is not None)):
            s = l1.val + l2.val
            if(isRemainder):
                s += 1
            node = ListNode(s % 10)
            if(lHead is None):
                lHead = node
                lCurrent = lHead
            else:
                lCurrent.next = node
                lCurrent = lCurrent.next
            isRemainder = (s > 9)
            l1 = l1.next
            l2 = l2.next
        
        # Add remaining linked lists
        while(l1 is not None):
            s = l1.val
            if(isRemainder):
                s += 1
            node = ListNode(s % 10)
            if(lHead is None):
                lHead = node
                lCurrent = lHead
            else:
                lCurrent.next = node
                lCurrent = lCurrent.next
            isRemainder = (s > 9)
            l1 = l1.next 
        while(l2 is not None):
            s = l2.val
            if(isRemainder):
                s += 1
            node = ListNode(s % 10)
            if(lHead is None):
                lHead = node
                lCurrent = lHead
            else:
                lCurrent.next = node
                lCurrent = lCurrent.next
            isRemainder = (s > 9)
            l2 = l2.next

        # Check if remainder is there even after both the linked list exhausted
        if(isRemainder):
            node = ListNode(1)
            lCurrent.next = node
            lCurrent = lCurrent.next
        return lHead