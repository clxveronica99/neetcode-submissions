class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if len(height) == 1:
            return res
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        while left < right:
            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                res += left_max - height[left]
                left += 1
            else:
                right_max = max(right_max, height[right])
                res += right_max - height[right]
                right -= 1
        return res



