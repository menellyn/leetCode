class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([el for el in s if el.isalnum()])

        right = len(s) - 1
        left = 0

        while left < right:
            if s[right] != s[left]:
                return False
            right -= 1
            left += 1
        
        return True