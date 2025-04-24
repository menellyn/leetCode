class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        rows = len(matrix)
        columns = len(matrix[0])

        left_board = 0
        right_board = columns - 1
        upper_board = 0
        lower_board = rows - 1

        total = rows*columns

        while len(ans) < total:
            for j in range(left_board, right_board + 1):
                if len(ans) < total:
                    ans.append(matrix[upper_board][j])
            upper_board += 1
            for i in range(upper_board, lower_board + 1):
                if len(ans) < total:
                    ans.append(matrix[i][right_board])
            right_board -= 1
            for j in range(right_board, left_board - 1, -1):
                if len(ans) < total:
                    ans.append(matrix[lower_board][j])
            lower_board -= 1
            for i in range(lower_board, upper_board - 1, -1):
                if len(ans) < total:
                    ans.append(matrix[i][left_board])
            left_board += 1

        return ans