class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x):
            if i**2 == x:
                return i
            elif i**2<x<((i+1)**2):
                return i
        return x