class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        empty_list = []
        for i in nums1:
            if i in nums2:
                empty_list.append(i)
                nums2.remove(i)
        return empty_list
