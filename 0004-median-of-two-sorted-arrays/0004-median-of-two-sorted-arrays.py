class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        c = nums1 + nums2
        c.sort()
        n = len(c)

        if n%2==1:
            return c[n//2]
        else:
            return (c[(n//2)-1]+c[n//2])/2