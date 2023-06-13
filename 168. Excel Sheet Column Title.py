class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        final_string = ""
        while columnNumber > 0:
            columnNumber = columnNumber - 1
            final_string = letter[columnNumber%26] + final_string
            columnNumber = columnNumber // 26
        return final_string
