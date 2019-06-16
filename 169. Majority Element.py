# day 37 2019-06-15 Sat
# 169. Majority Element

# Approach 1
class Solution:
    def majorityElement(self, nums) -> int:
        length = len(nums)
        if length < 2:
            return nums[0]
        nums.sort()
        count = 1
        for i in range(length-1):
            if nums[i] == nums[i+1]:
                count += 1
                if count > length//2:
                    return nums[i]
            else:
                count = 1

# Approach 2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # print(dir(list))
        length = len(nums)
        if length < 2:
            return nums[0]
        numsNew = set(nums)
        for i in numsNew:
            if nums.count(i) > length//2:
                return i



