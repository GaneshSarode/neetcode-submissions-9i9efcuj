class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        k = 0
        seen = set(nums)
        for i in nums:
            if (i-1) not in seen:
                l = 0
                while (i+l) in seen:
                    l+=1
                k = max(k,l)
        return k