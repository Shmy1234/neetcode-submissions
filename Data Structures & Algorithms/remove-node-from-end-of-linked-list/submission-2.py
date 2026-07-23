# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        l = 0
        while node:
            l+=1
            node=node.next
        
        if head is None:
            return []
        elif l-n==0:
            return head.next
        
        prev = ListNode
        node = head
        nxt = head.next
        counter = 0
        
        while nxt:
            if counter == l - n:
                prev.next = nxt
                break
            counter += 1
            prev, node, nxt = node, nxt, nxt.next
        return head


