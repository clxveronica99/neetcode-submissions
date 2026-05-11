class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashmap = {}
        for i in range(n):
            curr = nums[i]
            if target-curr in hashmap:
                return [hashmap[target-curr], i]
            hashmap[curr] = i
        return [-1, -1]
        

        