# day 40 2019-06-18 Tue
# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) < 2:
        #     return False
        # nums.sort();
        # ahead  = nums[0]
        # behind = nums[1]
        # for i in nums[2:]:
        #     if ahead == behind: return True
        #     behind = ahead
        #     ahead = i
        # if behind == ahead: return True
        # return False
        
        return len(nums) > len(set(nums))