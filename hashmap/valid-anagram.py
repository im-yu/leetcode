class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}
        if len(s) != len(t):
            return False
        for i in s:
            hashmaps[i] = hashmaps.get(i,0)+1
        for i in t:
            hashmapt[i] = hashmapt.get(i,0)+1
        if hashmaps == hashmapt:
            return True
        else: return False
