class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        m = {}
        for i in s:           
            seen[i] = seen.get(i,0)+1
        for k in t:
            m[k] = m.get(k,0)+1
        if seen==m:
            return True
        else: return False