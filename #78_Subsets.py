# day 23 2019-06-01 Sat
# 78. Subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subs = [[]]
        for i in range(len(nums)):
            subs += [s + [nums[i]] for s in subs]
        return subs