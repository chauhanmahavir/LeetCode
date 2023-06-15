class Solution:
    def intToRoman(self, num: int) -> str:
        roman_list = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
        ]

        result = ""

        for symbol, value in roman_list[::-1]:
            if num // value != 0:
                count = num // value
                result = result + (symbol * count)
                num = num % value
        return result
