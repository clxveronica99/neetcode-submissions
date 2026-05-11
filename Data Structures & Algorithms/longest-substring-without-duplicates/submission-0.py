import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        n = len(s)
        counter = collections.defaultdict(int)
        res = 0

        while right < n:
            counter[s[right]] += 1

            while left < right and counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
            right += 1
        return res

        

                
        