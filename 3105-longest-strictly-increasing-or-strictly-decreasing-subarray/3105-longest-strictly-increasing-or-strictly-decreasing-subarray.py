class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        longest = 1
        for i in range(1,len(nums)):

            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1

            elif nums[i] < nums[i-1]:
                inc = 1
                dec += 1

            else:
                inc = dec = 1

            longest = max(inc,dec,longest)
            
        return longest    