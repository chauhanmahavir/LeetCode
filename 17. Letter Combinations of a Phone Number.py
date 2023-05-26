class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dial_digits = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs" , "8" : "tuv", "9" : "wxyz"}
        res = []

        def backtrack(i, current_string):
            if len(current_string) == len(digits):
                res.append(current_string)
                return
            
            for char in dial_digits[digits[i]]:
                backtrack(i+1, current_string + char)
        
        if digits:
            backtrack(0, "")
            return res
        else:
            return []
