class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        new_s = []
        for i in range(len(s) - 1, -1, -1):
            new_s.append(s[i])
        
        return " ".join(new_s)