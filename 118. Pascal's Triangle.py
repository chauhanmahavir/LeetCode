class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        default_list = [[1]]
        if numRows > 1:
            for i in range(1, numRows + 1):
                sub_list = []
                for j in range(i):
                    if j == 0 or j == i-1:
                        sub_list.append(1)
                    else:
                        print(i, j)
                        sub_list.append(default_list[i-1][j] + default_list[i-1][j-1])
                print(sub_list)
                default_list.append(sub_list)
            return default_list[1:]
        else:
            return default_list
