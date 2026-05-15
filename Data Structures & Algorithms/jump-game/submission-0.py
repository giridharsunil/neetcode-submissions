class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastindex = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= lastindex:
                lastindex = i
        return lastindex == 0