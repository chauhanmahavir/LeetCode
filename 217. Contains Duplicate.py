class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        empty_dict = {}

        for i in nums:
            try:
                empty_dict[i] = empty_dict[i] + 1
                if empty_dict[i] >= 2:
                    return True
                    break
            except Exception as e:
                empty_dict[i] = 1
        else:
            return False
