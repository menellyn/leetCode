class Solution:
    def intToRoman(self, num: int) -> str:
        int_rom = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I'),
        ]

        roman = ""

        for val, sym in int_rom:
            if num == 0:
                break
            count = num // val
            roman += sym * count
            num -= val * count

        return roman