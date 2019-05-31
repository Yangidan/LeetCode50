# day 21 2019-05-30 Thu
# 62. Unique Paths
# DP method
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [[0]*m]*n
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i == n-1 and j == m-1:
                    mem[i][j] = 1
                elif i == n-1:
                    mem[i][j] = mem[i][j+1]
                elif j == m-1:
                    mem[i][j] = mem[i+1][j]
                else:
                    mem[i][j] = mem[i+1][j] + mem[i][j+1]
        return mem[0][0]