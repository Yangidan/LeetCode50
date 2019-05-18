# day 08 2019-05-17 Fri
# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        minLenInStrs = 2**32
        # find out the shortest string in strs: minLenStr
        for eachStr in strs:
            minLenInStrs = min(len(eachStr),minLenInStrs)
            if minLenInStrs == len(eachStr): 
                minLenStr = eachStr
        res = []
        flg = True
        for idx in range(minLenInStrs):
            for eachStrN in strs:
                if minLenStr[idx] != eachStrN[idx]:
                    flg = False
                    break
            if flg:
                res.append(minLenStr[idx])
            else:
                break
        return ''.join(res)