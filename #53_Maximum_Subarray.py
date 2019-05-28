# day 17 2019-05-27 Mon
# 53.Maximum_Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if (len(nums) < 1):
            return 0
        
        bestSum = nums[0]
        Sum = nums[0]
        
        for i in range(1,len(nums)):
            Sum = max(Sum + nums[i], nums[i])
            bestSum = max(bestSum, Sum)
        return bestSum