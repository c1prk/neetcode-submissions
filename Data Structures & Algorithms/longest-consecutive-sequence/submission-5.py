class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2, 20, 4, 10, 3, 4, 5
        res = 0
        test = set(nums)
        for i in range(len(nums)):
            if (nums[i]-1) not in test:
                temp = 1
                while nums[i]+temp in test:
                    temp+=1
                res = max(temp,res)
        return res
