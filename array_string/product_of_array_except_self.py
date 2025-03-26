class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1 for _ in range(len(nums))]

        prefix = suffix = 1

        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer