import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        counter2 = collections.defaultdict(int)
        n1, n2 = len(s1), len(s2)

        left, right = 0, 0
        while right < n2:
            counter2[s2[right]] += 1
            while left <= right and counter2[s2[right]] > counter1[s2[right]]:
                counter2[s2[left]] -= 1
                if counter2[s2[left]] == 0:
                    del counter2[s2[left]]
                left += 1
            
            if right - left + 1 == n1 and counter1 == counter2:
                return True
            right += 1
        return False

        