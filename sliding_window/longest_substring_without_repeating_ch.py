class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        characters = set()

        for right in range(len(s)):

            if s[right] in characters:
                if right - left > max_len:
                    max_len = right - left
                
                while s[left] != s[right]:
                    characters.remove(s[left])
                    left += 1

                characters.remove(s[left])
                left += 1
            
            characters.add(s[right])

        return max(max_len, len(characters))