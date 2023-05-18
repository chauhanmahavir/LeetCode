class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final_list = nums1 + nums2
        final_list.sort()
        if len(final_list) % 2 != 0:
            return final_list[len(final_list)//2]
        else:
            return (final_list[len(final_list)//2] + final_list[len(final_list)//2-1])/2