# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def swapPairs(self, head: ListNode) -> ListNode:
#         dummy = ListNode(-1)
#         dummy.next = head
#         tmp = dummy
#         while head  and head.next:
#             node_1 = head
#             node_2 = head.next
#
#             tmp.next = node_2
#             node_1.next = node_2.next
#             node_2.next = node_1
#
#             tmp = node_1
#             head = tmp.next
#         return dummy.next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if  not head or not head.next:
            return head
        node_1 = head
        node_2 = head.next
        node_1.next = self.swapPairs(node_2.next)
        node_2.next = node_1.next
        return node_2




