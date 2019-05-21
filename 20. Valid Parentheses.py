# day 11 2019-05-20 Mon
# 20. Valid Parentheses
# stack
class Solution:
    def isValid(self, s: 'str') -> 'bool':
        symbol_pairs={'(':')','[':']','{':'}'}
        s=list(s)
        opening=[]
        
        i=0
        while i<len(s):
           # print(i)
            
            
            if s[i] in (symbol_pairs.keys()):
                #print('db')
                opening.append(s[i])
            if s[i] in list(symbol_pairs.values()):
                if len(opening)!=0 and symbol_pairs[opening[-1]]==s[i]:
                    opening.pop()
                else:
                    return False
            i=i+1
        if len(opening)==0:
            return True
        else:
            return False