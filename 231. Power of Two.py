# day 42 2019-06-20 Thu
# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        while 2**i < n:
            i += 1
        if 2**i == n:
            return True
        return False