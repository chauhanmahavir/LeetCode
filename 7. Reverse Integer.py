class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reversed = int(str(x)[::-1])
            return reversed if -2**31 <= reversed < 2**31 else 0
        else:
            reversed = -int(str(x)[1::][::-1])
            return reversed if -2**31 <= reversed < 2**31 else 0
