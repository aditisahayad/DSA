class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        rows = {}

        # Reserved seats ko row-wise store karo
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Jo rows completely free hain
        ans = (n - len(rows)) * 2

        # Sirf reserved rows check karo
        for seats in rows.values():

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            can_left = seats.isdisjoint(left)
            can_middle = seats.isdisjoint(middle)
            can_right = seats.isdisjoint(right)

            # Left + Right dono possible
            if can_left and can_right:
                ans += 2

            # Koi ek block possible
            elif can_left or can_middle or can_right:
                ans += 1

        return ans