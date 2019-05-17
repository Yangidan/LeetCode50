# day 07 2019-05-16 Thu
# 11. Container With Most Water
# --> <--
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res, first = 0, 0
        last = len(height)-1
        while first < last:
            res = max(res, min(height[first], height[last])*(last-first))
            if height[first] <= height[last]:
                first += 1
            else:
                last -= 1
        return res