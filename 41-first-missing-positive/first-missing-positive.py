class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        '''num=list(range(1,len(nums)+2))[::-1]
        res=0
        for i in range(len(nums)):
            if nums[i] != num[-1]:
                if nums[i] in num:
                    num.remove(nums[i])
                res=num[-1]
            else:
                num.remove(num[-1])
                res=num[-1]
        return res'''

        seen=set()
        res=1
        for i in range(len(nums)):
            seen.add(nums[i])
            while res in seen:
                res+=1
        return res