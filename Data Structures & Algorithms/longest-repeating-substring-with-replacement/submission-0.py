class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        left, right = 0, 0
        counter = [0] * 26
        max_f = 0
        res = 0
        while right < n:
            counter[ord(s[right])-ord('A')] += 1
            max_f = max(max_f, counter[ord(s[right])-ord('A')])

            if (right - left + 1) - max_f > k:
                counter[ord(s[left]) - ord('A')] -= 1
                left += 1
            
            res = max(res, right - left + 1)
            right += 1
        return res



        