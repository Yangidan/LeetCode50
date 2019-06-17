# day 38 2019-06-16 Sun
# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l = list(reversed(l))

        head = ListNode(l[0])
        phead = head
        for i in l[1:]:
            head.next = ListNode(i)
            head = head.next
        return phead
