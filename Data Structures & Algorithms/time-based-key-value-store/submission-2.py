import collections
class TimeMap:

    def __init__(self):
        self.storage = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ''
        res = ''
        left, right = 0, len(self.storage[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.storage[key][mid][0] <= timestamp:
                res = self.storage[key][mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return res

        
