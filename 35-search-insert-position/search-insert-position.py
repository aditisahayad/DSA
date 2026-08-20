class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i=0
        while i<n:
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i
            else: 
                i+=1
        return n