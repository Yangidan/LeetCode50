# day 10 2019-05-19 Sun
# 16. 3Sum Closest
class Solution:
    def threeSumClosest(self, nums , target: int) -> int:
        nums.sort()
        sprev = nums[0]+nums[1]+nums[-1]
        for i in range(len(nums)-2):
            l,r=i+1,len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s == target:
                    return s
                if abs(s-target) < abs(sprev - target):
                    sprev=s
                if s < target:
                    l=l+1
                elif s > target:
                    r=r-1

        return sprev