class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        m = 1
        while n>0:
            rem = n%10
            s += rem
            m *= rem
            n //= 10
        return m - s
        