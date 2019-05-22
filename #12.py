# day 12 2019-05-21 Tue
# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        Head = ListNode(0)
        pHead = Head
        l1end = False
        l2end = False
        while (1):
            if l1.val <= l2.val:
                pHead.next = l1
                pHead = pHead.next
                if l1.next == None:
                    pHead.next = l2
                    break
                l1 = l1.next
                # print("%d ;"%l1.val)
                
            else:
                pHead.next = l2
                pHead = pHead.next
                if l2.next == None:
                    pHead.next = l1
                    break
                l2 = l2.next
        return Head.next