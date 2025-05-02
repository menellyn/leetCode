class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_idx = {}
        t_idx = {}

        for i in range(len(s)):
            if s[i] not in s_idx:
                s_idx[s[i]] = i

            if t[i] not in t_idx:
                t_idx[t[i]] = i

            if s_idx[s[i]] != t_idx[t[i]]:
                return False

        return True