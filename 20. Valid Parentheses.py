class Solution:
    def isValid(self, s: str) -> bool:
        empty_list = []
        open_close_dict = {"(" : ")", ")" : "(", "{" : "}", "}" : "{", "[" : "]", "]" : "["}
        if len(s) % 2 == 0:
            for i in s:
                if i in ["(", "{", "["]:
                    empty_list.append(i)
                elif i in ["}", "]", ")"]:
                    if len(empty_list) != 0 and empty_list[-1] == open_close_dict[i]:
                        del empty_list[-1]
                    else:
                        return False            
            if len(empty_list) == 0:
                return True
            else:
                return False
        else:
            return False
