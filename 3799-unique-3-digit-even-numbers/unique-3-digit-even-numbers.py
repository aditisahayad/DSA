class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        # Count how many times each digit occurs
        for d in digits:
            count[d] += 1

        ans = []

        # Try every possible 3-digit number
        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Check whether required digits are available
            used = [0] * 10
            used[a] += 1
            used[b] += 1
            used[c] += 1

            if all(used[d] <= count[d] for d in range(10)):
                ans.append(num)

        return len(ans)