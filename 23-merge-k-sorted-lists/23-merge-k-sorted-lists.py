import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(h)
        head = None
        while(h):
            val, idx = heapq.heappop(h)
            if(head is None):
                head = ListNode(val)
                current = head
            else:
                current.next = ListNode(val)
                current = current.next
            lists[idx] = lists[idx].next
            if(lists[idx]):
                heapq.heappush(h, (lists[idx].val, idx))
        return head