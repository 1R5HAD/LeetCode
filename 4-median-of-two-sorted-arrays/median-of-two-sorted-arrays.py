class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums3=sorted(nums1+nums2)
        n=len(nums3)
        if n%2!=0:
            return nums3[n//2]
        else:
            return (nums3[int(n/2)-1] + nums3[int(n/2)]) / 2

            
