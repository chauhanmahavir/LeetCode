class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        default_list = [[1]]
        if rowIndex >= 1:
            for i in range(1, rowIndex + 2):
                sub_list = []
                for j in range(i):
                    if j == 0 or j == i-1:
                        sub_list.append(1)
                    else:
                        sub_list.append(default_list[i-1][j] + default_list[i-1][j-1])
                default_list.append(sub_list)
            return default_list[-1]
        else:
            return default_list[0]
