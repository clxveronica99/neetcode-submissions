import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = collections.Counter(nums)

        bucket = [[] for _ in range(n+1)]
        res = []
        for num, freq in counter.items():
            bucket[freq].append(num)
        
        for i in range(n, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res