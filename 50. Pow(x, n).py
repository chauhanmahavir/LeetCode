class Solution:
    def myPow(self, x: float, n: int) -> float:
        def function(x, n):
            if n == 0:
                return 1
            elif n % 2 == 0:
                return function(x * x, n // 2)
            else:
                return x * function(x * x, (n-1)//2)
        f = function(x, abs(n))

        return float(f) if n >= 0 else 1/f
