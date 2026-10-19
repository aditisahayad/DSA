class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        ans=[]
        nums.sort()
        for i in range(n):
            if nums[i] == target:
                ans.append(i)
        return ans
        