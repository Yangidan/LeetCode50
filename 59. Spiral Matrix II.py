# day 49 2019-06-27 Thu
# 59. Spiral Matrix II

class Solution(object):
    def generateMatrix(self, n):
        res = [[0 for _ in xrange(n)] for _ in xrange(n)]
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        x, y = 0, 0
        for i in xrange(n * n):
            res[x][y] = i + 1
            next_x, next_y = x + dir[cur_dir][0], y + dir[cur_dir][1]
            if next_x >= n or next_y >= n or res[next_x][next_y]:
                cur_dir = (cur_dir + 1) % 4
            x, y = x + dir[cur_dir][0], y + dir[cur_dir][1]
        return res