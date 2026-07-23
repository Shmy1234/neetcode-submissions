# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2
        if node1 and not node2:
            return node1
        elif node2 and not node1:
            return node2
        else:
            if node1.val > node2.val:
                head = ListNode(node1.val)
                node1 = node1.next
            else:
                head = ListNode(node2.val)
                node2 = node2.next
        
        node = head

        while node1 and node2:
            if node1.val < node2.val:
                node.next = ListNode(node1.val)
                node1 = node1.next
            else:
                node.next = ListNode(node2.val)
                node2 = node2.next
            node = node.next
        
        if node1 and not node2:
            node.next = node1
        elif node2 and not node1:
            node.next = node2
        
        return head
        




