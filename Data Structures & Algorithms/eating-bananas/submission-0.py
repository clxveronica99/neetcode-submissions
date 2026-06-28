class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_total(threshold):
            count = 0
            for p in piles:
                d = p // threshold
                d = d + 1 if p % threshold != 0 else d
                count += d
            return count

        n = len(piles)
        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if get_total(mid) <= h:
                high = mid - 1
            else:
                low = mid + 1
        return low
        