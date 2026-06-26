class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        K = 0
        for i in range (len(nums)):
            if val!=nums[i]:
                nums[K] = nums[i]
                K +=1
        
        return K