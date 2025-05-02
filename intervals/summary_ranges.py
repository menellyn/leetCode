class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []

        if len(nums) == 0:
            return ans

        ptr = 0

        for i in range(len(nums) + 1):
            if i == len(nums) or nums[i] - nums[ptr] != i - ptr:
                if i - 1 != ptr:
                    ans.append(f"{nums[ptr]}->{nums[i-1]}")
                else:
                    ans.append(str(nums[ptr]))
                ptr = i  

        return ans   