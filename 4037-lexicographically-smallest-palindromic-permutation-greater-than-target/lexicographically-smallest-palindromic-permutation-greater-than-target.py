class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters in s
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - 97] += 1

        # A palindrome can have at most one odd frequency
        odd = 0
        middle = ""

        for i in range(26):
            if freq[i] % 2:
                odd += 1
                middle = chr(i + 97)

        if odd > 1:
            return ""

        # Frequency available for the left half
        half_freq = [x // 2 for x in freq]

        m = n // 2

        # Target's first half
        target_half = target[:m]

        candidates = []

        # --------------------------------------------------
        # Case 1:
        # Try making the left half strictly greater than
        # target_half at some position.
        # --------------------------------------------------

        for pivot in range(m - 1, -1, -1):

            # Start with all characters available
            remaining = half_freq[:]

            # Build prefix = target_half[:pivot]
            possible = True

            for i in range(pivot):
                c = ord(target_half[i]) - 97

                if remaining[c] == 0:
                    possible = False
                    break

                remaining[c] -= 1

            if not possible:
                continue

            # At pivot, choose the smallest character
            # strictly greater than target[pivot]
            current = ord(target_half[pivot]) - 97

            bigger = -1

            for c in range(current + 1, 26):
                if remaining[c] > 0:
                    bigger = c
                    break

            if bigger == -1:
                continue

            # Construct left half
            left = target_half[:pivot] + chr(bigger + 97)

            remaining[bigger] -= 1

            # Fill remaining positions with smallest characters
            for c in range(26):
                while remaining[c] > 0:
                    left += chr(c + 97)
                    remaining[c] -= 1

            # Make palindrome
            palindrome = left + middle + left[::-1]

            if palindrome > target:
                candidates.append(palindrome)

        # --------------------------------------------------
        # Case 2:
        # Left half is exactly target_half.
        # The complete palindrome may still be > target
        # because of middle/right side.
        # --------------------------------------------------

        remaining = half_freq[:]
        possible = True

        for ch in target_half:
            c = ord(ch) - 97

            if remaining[c] == 0:
                possible = False
                break

            remaining[c] -= 1

        if possible:
            left = target_half
            palindrome = left + middle + left[::-1]

            if palindrome > target:
                candidates.append(palindrome)

        # --------------------------------------------------
        # Return smallest valid answer
        # --------------------------------------------------

        if not candidates:
            return ""

        return min(candidates)