# day 09 2019-05-18 Sat
# 15. 3Sum
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        results = set()
        for i,a in enumerate(nums[:-2]):
            if i >= 1 and a == nums[i-1]:
                continue
            target = -a
            dict_map = {}
            # now the target is fixed,we solve the twosum problem
            for j,b in enumerate(nums[i+1:]):
                if b in dict_map:
                    results.add((a,b,target-b))
                else:
                    dict_map[target - b] = j
        return list(map(list,results))