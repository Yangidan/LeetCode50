# day 29 2019-06-07 Fri
# 136. Single Number
class Solution:
    def singleNumber(self, nums) -> int:
        nums.sort()
        print(nums)
        if len(nums) < 4:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        for i in range(len(nums)-2):
            if nums[i] != nums[i+1] and nums[i+1] != nums[i+2]:
                return nums[i+1]
            else:
                continue
def main():
    while True:
        try:
            prices = [2,2,4,3,3,3,5,5]
            
            ret = Solution().singleNumber(prices)

            print(ret)
            break
        except StopIteration:
            break

if __name__ == '__main__':
    main()