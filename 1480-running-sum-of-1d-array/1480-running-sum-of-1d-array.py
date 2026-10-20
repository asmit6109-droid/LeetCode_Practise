class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        a = []
        sum = 0
        for i in range(0,len(nums)):
            sum += nums[i]
            a.append(sum)
        return a
