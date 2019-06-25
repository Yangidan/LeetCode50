# day 46 2019-06-24 Mon
# 238. Product of Array Except Self

# [a，b，c，d，e]
# 从左乘一遍得到[1, a, ab, abc, abcd]
# 从右乘一遍得到[bcde,acde,abde,abce,abcd]
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        mul = 1
        for i in range(1, len(nums)):
            res.append(res[i-1]*nums[i-1])
        for i in range(len(nums)-2, -1, -1):
            mul *= nums[i+1]
            res[i] *= mul
        return res