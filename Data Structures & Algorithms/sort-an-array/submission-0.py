class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        m = len(nums)//2
        L = self.sortArray(nums[:m])
        R = self.sortArray(nums[m:])
        j , k = len(L),len(R)
        l , r = 0,0
        ans = []
        while l<j or r<k:
            if r>=k or l<j and L[l]<R[r]:
                ans.append(L[l])
                l +=1
            else:
                ans.append(R[r])
                r +=1
        return ans