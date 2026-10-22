class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, count, total,freq = 0,0,0,0
        hmap = defaultdict(int)
        for right in range(len(s)):
            hmap[s[right]]+=1
            freq = max(hmap[s[right]],freq)
            while(right-left+1)-freq>k:
                hmap[s[left]]-=1
                left+=1
            total = max(total,right-left+1)
            
        return total