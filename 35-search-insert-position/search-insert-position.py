class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif nums[i]>target and nums[i-1]<target:
                return i
            elif nums[i]>target and nums[i]==nums[0]:
                return i
            elif nums[i]<target and nums[i]==nums[-1]:
                return i+1