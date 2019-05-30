# day 20  2019-05-29 Wed
# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        lenNode = 0

        pHead = head
        temp = head
        while pHead:
            lenNode += 1
            if pHead.next is None:
                temp = pHead
            pHead = pHead.next
        if lenNode is 0:
            return head
        # if the length is eq to k: return list
        if k == lenNode:
            return head
        # MAKE A CIRCLE HERE
        temp.next = head
        # if k is bigger than the length of list, then take the mod result.
        k = k % lenNode
        numK = lenNode - k
        pHead = head
        while (numK-1) != 0:
            pHead = pHead.next
            numK -= 1
        head = pHead.next
        pHead.next = None
        return head
