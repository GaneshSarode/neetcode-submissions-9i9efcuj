class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cur = []
        for i in range(n):
            cur.append((position[i],speed[i]))
        cur.sort(reverse=True)
        stack = []
        for p,s in cur:
            time = (target-p)/s
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)