class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        sum = 0
        left = 0

        for right in range(len(nums)):
            sum += nums[right]
            
            while sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1

                sum -= nums[left]
                left += 1
            
        
        return min_len if min_len != float('inf') else 0