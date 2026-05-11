class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            while stack and stack[-1][1] < temperatures[i]:
                idx, val = stack.pop()
                res[idx] = i - idx
            stack.append((i, temperatures[i]))
        return res