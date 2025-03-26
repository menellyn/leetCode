class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        cnt = 0
        tmp = nums[0]
        for el in nums:
            if tmp != el:
                tmp = el
                cnt = 0
            if cnt < 2:
                nums[idx] = el
                cnt += 1
                idx += 1
            
        return idx