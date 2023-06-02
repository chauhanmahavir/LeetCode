class Solution:
    def addDigits(self, num: int) -> int:
        def devide(number):
            sum = 0
            print(number)
            for i in str(number):
                sum = sum + int(i)
            if sum > 9:
                return devide(sum)
            else:
                return sum
        return devide(num)
