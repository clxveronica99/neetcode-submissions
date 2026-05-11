class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left2right, right2left = [1] * n, [1] * n
        for i in range(1, n):
            left2right[i] = left2right[i - 1] * nums[i - 1]
        
        for i in range(n-2, -1, -1):
            right2left[i] = right2left[i + 1] * nums[i + 1]
        
        for i in range(n):
            left2right[i] *= right2left[i]
        return left2right
