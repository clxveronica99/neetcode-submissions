class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            num1 = nums[i]
            if num1 > 0:
                break
            if i > 0 and num1 == nums[i-1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                if num1 + nums[left] + nums[right] == 0:
                    res.append([num1, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif num1 + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return res

            
        