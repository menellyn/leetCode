class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))

        max_len = 0
        ptr = 0

        for i in range(len(nums)):
            if (nums[i] - nums[ptr]) != (i - ptr):
                if i - ptr > max_len:
                    max_len = i - ptr
                ptr = i
            elif i == len(nums) - 1 and i - ptr + 1 > max_len:
                max_len = i - ptr + 1

        return max_len