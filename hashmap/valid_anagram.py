from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
            
        counter = Counter(s)

        for el in t:
            if el not in counter or counter[el] <= 0:
                return False

            counter[el] -= 1

        return True