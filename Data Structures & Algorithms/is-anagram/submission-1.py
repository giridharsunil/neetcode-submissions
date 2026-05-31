class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        countt = {}
        for i in range(len(s)):
            if s[i] not in counts:
                counts[s[i]] = 1
            else:
                counts[s[i]] += 1
            if t[i] not in countt:
                countt[t[i]] = 1
            else:
                countt[t[i]] += 1
        return counts == countt
