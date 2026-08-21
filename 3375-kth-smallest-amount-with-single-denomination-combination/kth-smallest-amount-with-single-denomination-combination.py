from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            n = len(coins)
            total = 0

            for mask in range(1, 1 << n):
                multiple = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])

                        if multiple > x:
                            break

                        bits += 1
                else:
                    cnt = x // multiple

                    if bits % 2 == 1:
                        total += cnt
                    else:
                        total -= cnt

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left