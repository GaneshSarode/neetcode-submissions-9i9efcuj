class Solution:
    def isValid(self, s: str) -> bool:
        count = { ")" : "(" , "}" : "{" , "]" : "[" }
        stack = []
        for i in s:
            if i in count:
                if stack and stack[-1] == count[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False