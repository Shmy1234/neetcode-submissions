# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2
        if n1 is not None and n2 is None:
            return n1
        elif n1 is None and n2 is not None:
            return n2
        elif n1 is None and n2 is None :
            return None
        elif n1.val < n2.val:
            node = n1
            n1 = n1.next
        else: 
            node = n2
            n2 = n2.next
        
        h = node
        
        while n1 is not None or n2 is not None:
            if n1 is None and n2 is not None:
                node.next = n2 
                node = node.next
                n2 = n2.next
            elif n1 is not None and n2 is None:
                node.next = n1 
                node = node.next
                n1 = n1.next
            else:
                if n1.val < n2.val:
                    node.next = n1 
                    node = node.next
                    n1 = n1.next
                else:
                    node.next = n2 
                    node = node.next
                    n2 = n2.next
        
        return h







