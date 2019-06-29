# day 50 2019-06-28 Fri
# 557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        t = ""
        for i in s.split():
            # print(i[::-1])
            t += " "+''.join(i[::-1])
            # print(s)
        return t[1::]
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         return ' '.join(w[::-1] for w in s.split())