class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid
        def find_idx(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        if nums[left] == target:
            return left
        left_side = find_idx(0, left - 1)
        right_side = find_idx(left + 1, len(nums) - 1)
        if left_side == right_side:
            return -1
        return right_side if left_side == -1 else left_side

            
        