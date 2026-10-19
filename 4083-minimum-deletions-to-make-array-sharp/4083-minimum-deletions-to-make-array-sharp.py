class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                res +=1
        return res