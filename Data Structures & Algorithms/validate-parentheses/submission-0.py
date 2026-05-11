class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        n = len(s)
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            else:
                if not stack:
                    return False
                prev = stack.pop()
                if hashmap[ch] != prev:
                    return False
        return True if not stack else False

        


        