class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        new_s = ["" for _ in range(numRows)]
        i = 0
        reverse = False
        for letter in s:
            new_s[i] += letter
            if i == numRows - 1:
                reverse = True
            elif i == 0:
                reverse = False

            if reverse:
                i -= 1
            else:
                i += 1

        return "".join(new_s)