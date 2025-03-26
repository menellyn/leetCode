class Solution:
    def romanToInt(self, s: str) -> int:
        rom_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        num = 0
        l = len(s)

        for i in range(l):
            if i + 1 < l and rom_int[s[i]] < rom_int[s[i+1]]:
                num -= rom_int[s[i]]
            else:
                num += rom_int[s[i]]

        return num