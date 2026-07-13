class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        seen1 = {}

        for i in range(len(s)):
            seen[s[i]] = seen.get(s[i], 0) + 1

        for j in range(len(t)):
            seen1[t[j]] = seen1.get(t[j], 0) + 1

        return seen == seen1