class Solution:
    def search(self, nums: list[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            if target == nums[mid]:
                return mid

            elif target > nums[mid]:
                i = mid + 1

            else:
                j = mid - 1

        return -1
        
    #Recursive Way again solved it 
    class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        def BinarySearch(nums,low,high):
            if low > high:
                return -1
                
            mid = (low + high)//2
            
            if nums[mid] == target:
                return mid
                
            elif nums[mid] < target:
                return BinarySearch(nums,mid+1,high)
                
            elif nums[mid] > target:
                return BinarySearch(nums,low,mid-1)
                
        return BinarySearch(nums, low, high)
