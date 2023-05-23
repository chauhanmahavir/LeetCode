class Solution:
    def maxArea(self, height: List[int]) -> int:
        # max_water = 0
        # for left in range(len(height)):
        #     for right in range(left+1, len(height)):
        #         water = (min(height[left], height[right])) * (right-left)
        #         if water > max_water:
        #             max_water = water
        # return max_water

        left = 0
        right = len(height) - 1
        total_water = 0
        while left <= right:
            total = min(height[left], height[right]) * (right-left)
            total_water = max(total, total_water)
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
        return total_water
