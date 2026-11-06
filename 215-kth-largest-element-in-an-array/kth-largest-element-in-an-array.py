class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        lis=sorted(nums)
        return lis[-k]