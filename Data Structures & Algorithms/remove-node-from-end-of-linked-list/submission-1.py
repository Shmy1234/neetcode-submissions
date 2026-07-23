# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return []
        elif n==1:
            return head.next

        node = head
        l = 0
        while node:
            l+=1
            node=node.next
        
        prev = None
        node = head
        nxt = head.next
        counter = 1
        


        while nxt:
            if counter == l - n + 1:
                prev.next = nxt
                break
            counter += 1
            prev, node, nxt = node, nxt, nxt.next
        return head


