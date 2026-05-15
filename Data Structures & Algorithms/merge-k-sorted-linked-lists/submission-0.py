# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            node = lists[0]
            for i in range(1, len(lists)):
                node = self.mergeTwoLists(node, lists[i])
            return node
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2
        head = ListNode()
        node = head

        while node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node1 = node1.next 
            else:
                node.next = node2
                node2 = node2.next 
            node = node.next
        
        if node1: node.next = node1
        else: node.next = node2

        return head.next

        