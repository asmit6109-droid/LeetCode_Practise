class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        special = []

        for i in range(1,n+1):
            if n % i == 0:
                special.append(nums[i-1])

        sum_special = 0

        for j in special:
            sum_special += j * j
        
        return sum_special