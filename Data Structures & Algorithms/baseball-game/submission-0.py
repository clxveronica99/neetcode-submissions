class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for i in range(len(operations)):
            op = operations[i]
            if op.isdigit() or ('-' in op and op[1:].isdigit()):
                stack.append(int(op))
                res += int(op)
            elif op == 'C':
                res -= int(stack.pop())
            elif op == 'D':
                num = 2 * stack[-1]
                stack.append(num)
                res += num
            else:
                num1, num2 = stack[-1], stack[-2]
                s = num1 + num2
                stack.append(s)
                res += s
        return res