# day01 2019-05-10 Fri
# 2. Add Two Numbers
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = 0
        i = 0
        while (l1 != None or l2 != None):
            if (l1 is None):
                l1 = ListNode(0)
            if (l2 is None):
                l2 = ListNode(0)
                
            l3 += (l1.val + l2.val)*10**i
            l1 = l1.next
            l2 = l2.next
            i += 1
        l = []
        for i in str(l3):
            l.append(int(i))
        list.reverse(l)
        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in l:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummyRoot.next
        return ptr