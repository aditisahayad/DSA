class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a = []
        for i in range (len(nums)):
            c=0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    c+=1
            a.append(c)
        return a
                    