class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_el = {}

        for el in nums:
            if el not in count_el:
                count_el[el] = 0
            count_el[el] += 1
        
        for key, val in count_el.items():
            if val >= len(nums)/2:
                return key
        