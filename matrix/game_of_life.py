class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        def count_neighbors(row, col) -> int:
            count = 0
            for i in range(max(0, row-1), min(row+2, rows)):
                for j in range(max(0, col-1), min(col+2, cols)):
                    if i == row and j == col:
                        continue
                    else:
                        if abs(board[i][j]) == 1:
                            count += 1

            return count

        for i in range(rows):
            for j in range(cols):
                neighbors = count_neighbors(i, j)
                if board[i][j] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[i][j] = -1
                if board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 2

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1