class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        input_1_list = list(s)
        input_2_list = list(t)

        input_1_copy = input_1_list.copy()

        for i in input_1_list:
            if i in input_2_list:
                input_2_list.remove(i)
                del input_1_copy[0]
            else:
                return False
                break
        else:
            if len(input_1_copy) == len(input_2_list) == 0:
                return True
            else:
                return False
