# day 17 2019-05-26 Sun
# 46. Permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # a list of len 1 or less only has one permutation: itself
        if len(nums) <= 1:
            return [nums]
        else:
            perms = []
            
            # for each num n, compute all permutations that start with n
            for i, fst in enumerate(nums):
                
                # recursively compute all permutations of the remaining elements
                for perm in self.permute(nums[0:i] + nums[i+1:]):
                    perms.append([fst] + perm)
            return perms