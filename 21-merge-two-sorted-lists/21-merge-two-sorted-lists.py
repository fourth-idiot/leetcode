# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Approach 1
        # if((list1 is None) and (list2 is None)):
        #     return None
        # elif(list1 is None):
        #     return list2
        # elif(list2 is None):
        #     return list1
        # else:
        #     if(list1.val < list2.val):
        #         head = list1
        #         current = head
        #         list1 = list1.next
        #     else:
        #         head = list2
        #         current = head
        #         list2 = list2.next
        #     while((list1 is not None) and (list2 is not None)):
        #         if(list1.val < list2.val):
        #             current.next = list1
        #             list1 = list1.next
        #         else:
        #             current.next = list2
        #             list2 = list2.next
        #         current = current.next
        #     while(list1 is not None):
        #         current.next = list1
        #         current = current.next
        #         list1 = list1.next
        #     while(list2 is not None):
        #         current.next = list2
        #         current = current.next
        #         list2 = list2.next
        #     return head
        
        # Approach 2
        if(list1 is None):
            return list2
        elif(list2 is None):
            return list1
        elif(list1.val < list2.val):
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2