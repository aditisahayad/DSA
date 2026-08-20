class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
        elif n==0:
            return
        else:
            nums1[m:] = nums2
            nums1.sort()
        