class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        w = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                w.remove(nums[L])
                L +=1
            if nums[R] in w:
                return True
            w.add(nums[R])
        return False