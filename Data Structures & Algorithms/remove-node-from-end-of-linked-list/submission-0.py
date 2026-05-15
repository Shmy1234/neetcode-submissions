# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next 
            count += 1
        
        count -= n 
        if count < 0:
            return head
    
        count2 = 0
        prev = None
        curr = head
        while curr is not None:
            if count2 == count:
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next
            prev = curr
            curr = curr.next
            count2 += 1
        return head
