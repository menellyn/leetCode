class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sub_idx = 0
        sub_len = len(s)

        for i in range(len(t)):
            if sub_idx == sub_len:
                break
            if s[sub_idx] == t[i]:
                sub_idx += 1

        if sub_idx == sub_len:
            return True
        else:
            return False