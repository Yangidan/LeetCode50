# day 34 2019-06-12 Wed
# 148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        pH = head
        lH = []
        while pH:
            lH.append(pH.val)
            pH = pH.next
        lH.sort()
        pH = head
        for i in lH:
            head.next = ListNode(i)
            head = head.next
        
        return pH.next