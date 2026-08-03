class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            k = "".join(sorted(i))
            if k in res:
                res[k] = res[k] + [i]
            else:
                res[k] = [i]
        return list(res.values())