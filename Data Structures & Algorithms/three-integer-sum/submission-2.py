class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        res = []
        for i in range(len(sn)):
            mid = sn[i]
            if i>0 and mid==sn[i-1]:
                continue
            l,r=i+1,(len(nums)-1)
            while(r>l):
                total = mid+sn[l]+sn[r]
                if total == 0:
                    res.append([mid, sn[l], sn[r]])
                    l += 1
                    r -= 1
                    while l < r and sn[l] == sn[l - 1]:
                        l += 1
                    while l < r and sn[r] == sn[r + 1]:
                        r -= 1
                elif total > 0:
                    r-=1
                else:
                    l+=1
        return res



