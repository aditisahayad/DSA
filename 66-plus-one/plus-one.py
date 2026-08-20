class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = []
        num = int("".join(map(str, digits)))
        num = num+1
        while num>0:
            rem = num%10
            a.append(rem)
            num//=10
        return a[::-1]
        