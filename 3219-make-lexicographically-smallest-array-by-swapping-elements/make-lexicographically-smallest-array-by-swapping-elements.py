class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # value + original index
        arr = sorted((nums[i], i) for i in range(n))

        ans = nums[:]

        start = 0

        while start < n:
            end = start

            # Find one connected group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Values in this group are already sorted
            values = [arr[i][0] for i in range(start, end + 1)]

            # Original indices of this group
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Put smallest values at smallest indices
            for idx, value in zip(indices, values):
                ans[idx] = value

            start = end + 1

        return ans