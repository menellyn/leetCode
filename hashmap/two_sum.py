class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}

        for i in range(len(nums)):
            if target - nums[i] not in n:
                n[nums[i]] = i
            else:
                return [n[target - nums[i]], i]