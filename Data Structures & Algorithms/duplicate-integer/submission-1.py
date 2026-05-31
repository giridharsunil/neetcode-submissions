class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i]+=1
        if any(i>1 for i in hash.values()):
            return True
        else:
            return False