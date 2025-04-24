class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row_set = set()
        column_set = [set() for _ in range(9)]
        box_set = [set(), set(), set()]

        for i in range(9):
            row_set.clear()
            for j in range(9):
                digit = board[i][j]
                if digit != '.':
                    if digit not in row_set:
                        row_set.add(digit)
                    else:
                        return False
                    
                    if digit not in column_set[j]:
                        column_set[j].add(digit)
                    else:
                        return False

                    if digit not in box_set[j//3]:
                        box_set[j//3].add(digit)
                    else:
                        return False

            if (i+1)%3 == 0:
                for s in box_set:
                    s.clear()

        
        return True