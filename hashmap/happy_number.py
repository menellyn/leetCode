class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def next_number(n):
            out = 0

            while n:
                tmp = n % 10
                out += tmp**2
                n = n // 10

            return out

        while n not in visited:
            visited.add(n)
            n = next_number(n)
            if n == 1:
                return True

        return False