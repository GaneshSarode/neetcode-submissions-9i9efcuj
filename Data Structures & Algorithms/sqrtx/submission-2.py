class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        if x==1:
            return 1
        l , r = 0,x
        while l<=r and (r-l)>1:
            m = (l+r)//2
            if m*m==x:
                return m
            elif m*m>x:
                r=m
            else: l = m
        return l
        