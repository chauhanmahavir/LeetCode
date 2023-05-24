class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_list = []
        if len(nums) <= 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        else:
            nums.sort()
            # for i, v in enumerate(nums):
            #     for j, w in enumerate(nums[i+1:], start=i+1):
            #         for k, x in enumerate(nums[j+1:], start=j+1):
            #             triplet = [nums[i], nums[j], nums[k]]
            #             triplet.sort()
            #             if sum(triplet) == 0 and triplet not in final_list:
            #                 final_list.append(triplet)
            # return final_list
            
            for i, v in enumerate(nums):
                if i + 1 < len(nums):
                    left = i + 1
                    right = len(nums) - 1

                    while left < right:

                        triplet = [v, nums[left], nums[right]]

                        total = sum(triplet)

                        if total < 0:
                            left = left + 1
                        elif total > 0:
                            right = right - 1
                        elif triplet not in final_list:
                            final_list.append(triplet)
                            left = left + 1
                            right = right - 1
                        else:
                            left = left + 1
                            right = right - 1
            return final_list
