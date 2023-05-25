class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        empty_list = []

        for i,v in enumerate(nums):
            for j,w in enumerate(nums[i+1:], start=i+1):
                first_element = v
                second_element = w
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    third_element = nums[left]
                    fourth_element = nums[right]
                    sub_list = [first_element, second_element, third_element, fourth_element]
                    sub_list.sort()
                    if sum(sub_list) > target:
                        right = right - 1
                    elif sum(sub_list) < target:
                        left = left + 1
                    elif sub_list not in empty_list:
                        empty_list.append(sub_list)
                        left = left + 1
                        right = right - 1
                    else:
                        left = left + 1
                        right = right - 1
        return empty_list
