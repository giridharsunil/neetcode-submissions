class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = set()
        for i in range(len(nums)):
            if target - nums[i] in n:
                return [nums.index(target - nums[i]),i]
            else:
                n.add(nums[i])
        return False
