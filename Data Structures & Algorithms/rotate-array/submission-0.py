class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # (i+2) % len(nums)

        k = k%len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]