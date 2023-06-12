class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        empty_dict = {}

        for i in nums:
            try:
                empty_dict[i] = empty_dict[i] + 1
            except Exception as e:
                empty_dict[i] = 1
        for i in empty_dict:
            if empty_dict[i] == 1:
                return i
