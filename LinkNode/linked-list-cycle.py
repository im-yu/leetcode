# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None:
            return False
        target = {head}
        head = head.next
        while head:
            if head in target:
                return True
            else:
                target.add(head)
                head = head.next
        return False        #破坏链表了

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        target = set()
        node = head
        while node is not None:
            if node in target:
                return True
            else:
                target.add(node)
                node = node.next
        return False