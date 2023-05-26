class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() 
        diff = 20001
        total = 0
        for i, v in enumerate(nums):
            first = v
            left = i + 1
            right = len(nums) - 1
            while left < right:
                second = nums[left]
                third = nums[right]

                sub_list = [first, second, third]
                sub_diff = abs(sum(sub_list)-target)

                if sub_diff < diff:
                    diff = sub_diff
                    total = sum(sub_list)
                if sum(sub_list) == target:
                    return target
                elif sum(sub_list) < target:
                    left = left + 1
                else:
                    right = right - 1
        return total
