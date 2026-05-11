class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        hashmap = {
            '+': lambda a, b: a+b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b),
            '-': lambda a, b: a-b
        }
        
        for t in tokens:
            if t[0] == '-' and t[1:].isdigit() or t.isdigit():
                stack.append(int(t))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(hashmap[t](num2, num1))
        return stack[0]