# day04 2019-05-13 Mon
# 7. Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            # stringX = list(str(x))
            new_str = reversed(str(x))
            new_str = (str(x))[::-1]
            # print(new_str)
            outInteger = int(new_str)
            if (outInteger > 2**31-1) or (outInteger < -2**31):
                return 0
            return(outInteger)
            # print(stringX)
        else:
            # stringX = list(str(-x))
            # new_str = ''.join(reversed(stringX))
            new_str = (str(-x))[::-1]
            # print(new_str)
            outInteger = -int(new_str)
            if (outInteger > 2**31-1) or (outInteger < -2**31):
                return 0
            return(outInteger)
        a = int(str(x)[::-1]) if x >= 0 else -self.reverse(-x)
        return a if a < 2**31-1 else 0