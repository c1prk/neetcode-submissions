class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 2, 20, 4, 10, 3, 4, 5
        if len(nums)==0:
            return 0
        res = 1
        test = set(nums)

        for i in range(len(nums)):
            if (nums[i]-1) not in test:
                temp = 1
                j=nums[i]+1
                while j in test:
                    temp+=1
                    j+=1
                res = max(temp,res)
        return res
