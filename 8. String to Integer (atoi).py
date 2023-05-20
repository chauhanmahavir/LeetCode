class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        sign = 1

        if s == "":
            return 0

        if s[0] == "-" or s[0] == "+":
            sign = int(s[0]+str(sign))
            s = s[1:]
        
        final_string = "0"
        for i in s:
            if i.isnumeric():
                final_string = final_string + i
            else:
                break
        
        if sign*int(final_string) <= -2**31:
            return -2**31
        elif sign*int(final_string) >= 2**31 -1:
            return 2**31 - 1
        else:
            return sign*int(final_string)
        
