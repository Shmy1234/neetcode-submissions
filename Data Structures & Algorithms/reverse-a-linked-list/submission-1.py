# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        if node is None:
            return None
        nxt = node.next
        prev = None
        if nxt is None: 
            return node
        while nxt is not None:
            temp = nxt.next
            node.next, nxt.next = prev, node
            prev, node, nxt = node, nxt, temp

        return node
