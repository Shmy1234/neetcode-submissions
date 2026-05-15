# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return None

        node = head
        l = 0
        while node:
            l+=1
            node=node.next
        
        prev = None
        node = head
        counter = 0
        
        while node:
            if counter == l - n:
                if prev:
                    prev.next = node.next
                else:
                    head = node.next
                break
            counter += 1
            prev, node = node, node.next
        return head


