class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i=="+":
                val = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val+val1)
            elif i=="*":
                val = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(int(val*val1))
            elif i=="/":
                val = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1/val)
            elif i=="-":
                val = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1-val)
            else:
                stack.append(i)
        return int(stack[0])