class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        con = set()
        n = len(nums)
        for num in nums:
            if num in con:
                return True
            con.add(num)
        return False