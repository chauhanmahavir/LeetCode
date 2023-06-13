class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        empty_list = []
        for i in nums1:
            if i in nums2 and i not in empty_list:
                empty_list.append(i)
        return empty_list
