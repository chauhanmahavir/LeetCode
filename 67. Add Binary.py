class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_dict = {0 : "00", 1 : "01", 2 : "10", 3 : "11"}
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        i = len(a) - 1
        final_string = ""
        carry = 0
        
        while i >= 0:
            sum = int(a[i]) + int(b[i]) + carry
            carry = 0
            if sum == 0 or sum == 1:
                final_string = sum_dict[sum][1] + final_string
            elif sum > 1:
                carry = int(sum_dict[sum][0])
                final_string = sum_dict[sum][1] + final_string
            i = i - 1
        if carry != 0:
            return str(carry) + final_string
        else:
            return final_string
