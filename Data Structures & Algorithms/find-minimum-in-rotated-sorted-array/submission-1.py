class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3, 4, 5, 6, 1, 2]
        # [3, 4, 5] [6, 1 ,2]
        # l = 3, r = 2, mid = 5
        l, r = 0, len(nums)-1
        while l<r:
            m = l+(r-l)//2
            if nums[r]<nums[m]:
                l = m+1
            else:
                r=m
        return nums[r]
            