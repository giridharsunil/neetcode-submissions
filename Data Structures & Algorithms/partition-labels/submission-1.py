class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        map = {}
        for i in range(len(s)):
            if s[i] not in map:
                map[s[i]] = i
            else:
                map[s[i]] = i
        size = 0
        res = []
        lastindex = map[s[0]]
        for i in range(len(s)):
            size += 1
            lastindex = max(lastindex, map[s[i]])
            if i == lastindex:
                res.append(size)
                size = 0
        return res
            