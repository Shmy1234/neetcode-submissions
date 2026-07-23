# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        node = head
        l = []
        while node:
            l.append(node)
            node = node.next 
        
        for i in range(len(l)//2):
            temp = l[i].next 
            l[i].next = l[len(l) - i - 1]
            l[len(l) - i - 1].next = temp
            node = temp
        node.next = None


        