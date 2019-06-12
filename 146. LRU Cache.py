# day 33 2019-06-11 Tue 
# 146. LRU Cache

# get和put操作都为O(1)所以选择链表
# 这下面是From cy69855522：
# 有时间不用collection再自己实现一下。不过有轮子用着也挺好。
class LRUCache(object):

    def __init__(self, capacity):
        self.od, self.cap = collections.OrderedDict(), capacity

    def get(self, key):
        if key not in self.od: return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key, value):
        if key in self.od: del self.od[key]
        elif len(self.od) == self.cap: self.od.popitem(False)
        self.od[key] = value
