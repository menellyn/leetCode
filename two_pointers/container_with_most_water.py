class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0

        while left < right:
            tmp = min(height[right], height[left])*(right-left)
            if tmp > water:
                water = tmp
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return water