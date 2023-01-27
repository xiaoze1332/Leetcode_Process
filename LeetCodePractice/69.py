class Solution:
    def mySqrt(self, x: int) -> int:

        a = x // 2

        while(a > 0):
            if a ** 2 == x or (a ** 2 < x and (a + 1) ** 2 > x):
                return a
            elif a ** 2 > x:
                a = a // 2
            else:
                a = (a + x) // 2