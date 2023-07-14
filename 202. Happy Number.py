class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        def happy_number(num):
            if num > 0:
                sub_total = 0
                for i in str(num):
                    sub_total = sub_total + int(i)**2
                if sub_total == 1:
                    return True
                if sub_total in numbers:
                    return False
                else:
                    numbers.add(sub_total)
                    return happy_number(sub_total)
        return happy_number(n)
