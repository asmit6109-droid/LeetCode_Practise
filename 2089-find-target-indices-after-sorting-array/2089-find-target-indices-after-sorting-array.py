class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        n = len(nums)
        nums.sort()
        b = []

        for i in range(n):
            if nums[i] == target:
                b.append(i)
        return b