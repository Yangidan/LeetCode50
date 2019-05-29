# day 19 2019-05-28 Tue
# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        op = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_xy = (0, 0)
        cur_op = 0
        res = []
        height, width = len(matrix), len(matrix[0])
        while True:
            res.append(matrix[cur_xy[0]][cur_xy[1]])
            matrix[cur_xy[0]][cur_xy[1]] = ''
            tmp = (cur_xy[0] + op[cur_op][0], cur_xy[1] + op[cur_op][1])
            if not (0 <= tmp[0] < height and 0 <= tmp[1] < width and matrix[tmp[0]][tmp[1]] != ''):
                cur_op = (cur_op + 1) % 4
            cur_xy = (cur_xy[0] + op[cur_op][0], cur_xy[1] + op[cur_op][1])
            if not (0 <= cur_xy[0] < height and 0 <= cur_xy[1] < width and matrix[cur_xy[0]][cur_xy[1]] != ''):
                break
        return res