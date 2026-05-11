import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        hashmap = collections.defaultdict(list)
        for i in range(n):
            curr = strs[i]
            count = [0] * 26
            for c in curr:
                count[ord(c)-ord('a')] += 1
            hashmap[tuple(count)].append(curr)
        return list(hashmap.values())
