from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        ad = []
        result = {}
        for x in freq1:
            if x in freq2:
                a = min(freq1[x],freq2[x])
                result[x] = a
        for x in result:
            if result[x] > 0:
                ad.extend([x]*result[x])
        return ad

             

        