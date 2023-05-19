class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list_2d = [[] for _ in range(numRows)]
        forward = True
        index = 0
        final_string = ""
        if numRows == 1:
            return s
        for i in s:
            list_2d[index].append(i)
            if forward == True:
                index = index + 1
            if forward == False:
                index = index - 1
            if index > numRows - 1:
                forward = False
                index = index - 2
            if index < 0:
                forward = True
                index = index + 2
        for i in list_2d:
            final_string = final_string + "".join(i)
        return final_string