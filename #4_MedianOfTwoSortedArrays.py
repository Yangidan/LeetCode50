# day 02 2019-05-11 Sat
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Explaination: https://www.youtube.com/watch?v=LPFhl65R7ww&t=1013s
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        lt = l1 + l2
        if l1 is 0:
            return (nums2[int(l2/2)-1]+nums2[int(l2/2)])/2 if l2%2 is 0 else float(nums2[int(l2/2)])
        if l2 is 0:
            return (nums1[int(l1/2)-1]+nums1[int(l1/2)])/2 if l1%2 is 0 else float(nums1[int(l1/2)])
        return findMedianSortedArrays(nums1, nums2)
        
            
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    l1 = len(nums1)
    l2 = len(nums2)
    lt = l1 + l2
    if l1 > l2:
        return findMedianSortedArrays(nums2, nums1)
    
    start = 0
    end = l1
    while (start <= end):
        par1 = int((start+end)/2)
        par2 = int((l1+l2+1)/2) - par1
        # print(par1, par2, l1, l2)
        leftMax1 = float('-inf') if par1 is 0 else nums1[par1-1]
        rightMin1 = float('inf')  if par1 is l1 else nums1[par1]
        leftMax2 = float('-inf') if par2 is 0 else nums2[par2-1]
        rightMin2 =  float('inf')  if par2 is l2 else nums2[par2]

        if leftMax1 <= rightMin2 and leftMax2 <= rightMin1:
            res = float(max(leftMax1, leftMax2)) if lt%2 is 1 else (max(leftMax1, leftMax2) + min(rightMin1, rightMin2))/2
            return res
        elif leftMax1 > rightMin2:
            end = par1 - 1
        else:
            start = par1 + 1