class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        x = max(nums)
        for i in range(n):
            if nums[i] != x:
                count = count + (x-nums[i])
        return count   