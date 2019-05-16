# day 06 2019-05-15 Wed
# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = str(x)
        # flag = 0
        lenRes = len(res)
        for i in range(int(lenRes/2)):
            if res[i] != res[lenRes-i-1]:
                return False
        return True