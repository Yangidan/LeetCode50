# day 13 2019-05-22 Wed
# 23. Merge k Sorted Lists
def get_parent(i):
    return (i+1)//2 - 1

def right_child(i):
    return (i+1)*2

def left_child(i):
    return (i+1)*2 - 1

class Solution:
    def add(self, elem):
        self.h.append(elem)
        i = len(self.h) - 1
        parent = get_parent(i)
        while parent >= 0:
            if self.h[parent].val > self.h[i].val:
                self.swap(parent, i)
                i = parent
                parent = get_parent(i)
            else:
                break

    def get_min(self):
        n = len(self.h)
        if n == 0:
            return None
        i = 0

        res = self.h[0]
        self.swap(0, n-1)
        self.h.pop(n-1)
        n = n - 1
        while True:
            rc = right_child(i)
            lc = left_child(i)
            iv = self.v(i)
            rv = self.v(rc)
            lv = self.v(lc)
            if rc < n and lc < n:
                if iv < rv and iv < lv:
                    break
                if self.h[lc].val < self.h[rc].val:
                    self.swap(i, lc)
                    i = lc
                else:
                    self.swap(i, rc)
                    i = rc
            elif rc < n:
                if iv < rv:
                    break
                self.swap(i, rc)
                i = rc
            elif lc < n:
                if iv < lv:
                    break
                self.swap(i,lc)
                i = lc
            else:
                break
        return res

    def v(self, i):
        if i < len(self.h):
            return self.h[i].val
        return None

    def swap(self, i, j):
        tmp = self.h[i]
        self.h[i] = self.h[j]
        self.h[j] = tmp


    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        self.h = []
        for l in lists:
            if l is not None:
                self.add(l)

        x = self.get_min()
        first = x
        last = x
        while x is not None:
            next_item_in_list = x.next

            last.next = x
            x.next = None
            last = x

            if next_item_in_list is not None:
                self.add(next_item_in_list)
            x = self.get_min()
        return first