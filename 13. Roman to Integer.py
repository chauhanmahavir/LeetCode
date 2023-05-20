class Solution:
    def romanToInt(self, s: str) -> int:
        roman_digit = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        digit = 0
        index = 0
        while index <= len(s) - 1:
            #print(index)
            if index != len(s)-1 and roman_digit[s[index+1]] > roman_digit[s[index]]:
                digit = digit + roman_digit[s[index+1]] - roman_digit[s[index]]
                index = index + 1
            else:
                digit = digit + roman_digit[s[index]]
            index = index + 1
        return digit
