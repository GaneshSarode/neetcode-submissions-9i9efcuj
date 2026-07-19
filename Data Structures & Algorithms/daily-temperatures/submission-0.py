class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        answer = [0] * n
        l = 0
        while l < n:
            r = l + 1
            while r < n and temp[r] <= temp[l]:
                r += 1
            if r < n:
                answer[l] = r - l
            l += 1
        return answer