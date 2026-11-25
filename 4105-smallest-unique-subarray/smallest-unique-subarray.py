
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        BASE1, BASE2 = 100019, 100043
        MOD1, MOD2 = 10**9 + 7, 10**9 + 9

        def check(length):
            power1 = pow(BASE1, length, MOD1)
            power2 = pow(BASE2, length, MOD2)

            h1 = h2 = 0
            freq = {}

            for i in range(n):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2

                if i >= length:
                    h1 = (h1 - nums[i - length] * power1) % MOD1
                    h2 = (h2 - nums[i - length] * power2) % MOD2

                if i >= length - 1:
                    key = (h1, h2)
                    freq[key] = freq.get(key, 0) + 1

            return any(count == 1 for count in freq.values())

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
