class Solution:
    def isHappy(self, n: int) -> bool:
        def happy_number(num):
            if num > 0:
                sub_total = 0
                for i in str(num):
                    sub_total = sub_total + int(i)**2
                if sub_total > 9:
                    return happy_number(sub_total)
                elif sub_total == 1:
                    return True
                elif sub_total > 1 and sub_total <= 9:
                    return False
            else:
                return False
        return happy_number(n)
