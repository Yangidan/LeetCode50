# day03 2019-05-12 Sun
# 5. Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        lofs = len(s)
        if lofs < 2:
            return s
        for i in range(lofs):
            for j in range(i+1):
                if pchecker(s[j:lofs-i+j]):
                    return s[j:lofs-i+j]

def pchecker(sn:str)->bool:
    if sn != sn[::-1]:
        return False
    return True