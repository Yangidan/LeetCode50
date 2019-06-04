# day 25 2019-06-03 Mon
# 89. Gray Code
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ i >> 1  for i in range(1 << n)]