class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        l = len(nums)

        for i in range(l):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = l - 1
            while j < k:
                tmp = nums[i] + nums[j] + nums[k]
                if tmp == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif tmp > 0:
                    k -= 1
                else:
                    j += 1

        return ans