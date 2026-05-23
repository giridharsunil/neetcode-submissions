class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxone = 0
        count = 0
        for i in nums:
            if i == 1:
                count+=1
            elif i == 0:
                maxone = max(maxone, count)
                count = 0
            print(i,count)
        return max(count,maxone)