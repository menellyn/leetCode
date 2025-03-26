class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        used_el = set()
        for el in nums:
            if el not in used_el:
                nums[idx] = el
                used_el.add(el)
                idx += 1
                
        return idx