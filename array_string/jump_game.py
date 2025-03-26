class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reserve = 0

        for el in nums:
            if reserve < 0:
                return False
            if el > reserve:
                reserve = el
            
            reserve -= 1

        return True