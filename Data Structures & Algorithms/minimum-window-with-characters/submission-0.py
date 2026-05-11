import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        counter_t = collections.Counter(t)
        required = len(counter_t)
        formed = 0
        left, right = 0, 0
        res = float('inf'), 0, 0
        filtered = []
        for idx, val in enumerate(s):
            if val in counter_t:
                filtered.append((idx, val))
        window_count = {}
        while right < len(filtered):
            idx, char = filtered[right]
            window_count[char] = window_count.get(char, 0) + 1
            if window_count[char] == counter_t[char]:
                formed += 1
            while left <= right and formed == required:
                idx1, char1 = filtered[left]
                if idx - idx1 + 1 < res[0]:
                    res = idx - idx1 + 1, idx1, idx
                window_count[char1] -= 1
                if window_count[char1] < counter_t[char1]:
                    formed -= 1
                left += 1
            right += 1
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]
                    
