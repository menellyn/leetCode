class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()

        if len(s) != len(pattern):
            return False 
            
        p_idx = {}
        s_idx = {}

        for i in range(len(pattern)):

            if pattern[i] not in p_idx:
                p_idx[pattern[i]] = i
            
            if s[i] not in s_idx:
                s_idx[s[i]] = i

            if s_idx[s[i]] != p_idx[pattern[i]]:
                return False

        return True