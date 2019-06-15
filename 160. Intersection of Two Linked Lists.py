# day 36 2019-06-14 Fri
# 160. Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        return self.__getIntersectionVal(headA, headB)
    
    def __getIntersectionVal(self, headA, headB):
        lenA = self.__getLen(headA)
        lenB = self.__getLen(headB)

        pA, pB = headA, headB

        ret = 0
        
        if lenA > lenB:
            return self.__getIntersectionVal(headB, headA)
        
        pA, pB = headA, headB
        gap = lenB - lenA
        while gap:
            gap -= 1
            pB = pB.next
        while pA:
            if pA == pB:
                return pA
            if pA.next is None:
                return None
            pA, pB = pA.next, pB.next


    def __getLen(self, head):
        pH = head
        lenH = 0
        while pH:
            lenH += 1
            pH = pH.next
        return lenH