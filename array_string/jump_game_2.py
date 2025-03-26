class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = end = further = 0

        for i in range(len(nums)-1):
            further = max(further, i + nums[i])

            if i == end:
                jumps += 1
                end = further

        return jumps