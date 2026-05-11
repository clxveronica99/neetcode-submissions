class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        res = float('-inf')
        while left < right:
            h1, h2 = height[left], height[right]
            if h1 > h2:
                res = max(res, (right-left) * h2)
                right -= 1
            else:
                res = max(res, (right-left) * h1)
                left += 1
        return res