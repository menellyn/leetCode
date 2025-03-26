class Solution:
    def removeElement(self, nums, val: int) -> int:
        
        if val > 50:
            return len(nums)
        
        idx = 0
        for el in nums:
            if el != val:
                nums[idx] = el
                idx += 1
        
        return idx
    