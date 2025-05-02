from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for el in ransomNote:
            if el not in counter or counter[el] <= 0:
                return False
            counter[el] -=1
        
        return True