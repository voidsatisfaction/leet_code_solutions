from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_is_valid_val(board: List[List[str]], row: int, col: int) -> bool:
            val = board[row][col]
            # check row
            for i in range(9):
                if col == i:
                    continue

                another_val = board[row][i]
                if val == another_val:
                    return False

            # check col
            for i in range(9):
                if row == i:
                    continue

                another_val = board[i][col]
                if val == another_val:
                    return False

            # check 3x3 box
            box_row, box_col = (row // 3, col // 3)
            for r in range(3*box_row, 3*(box_row+1)):
                for c in range(3*box_col, 3*(box_col+1)):
                    if r == row and c == col:
                        continue

                    another_val = board[r][c]

                    if val == another_val:
                        return False

            return True

        for row in range(9):
            for col in range(9):
                if board[row][col] != '.' and check_is_valid_val(board, row, col) is False:
                    return False

        return True
                    
if __name__ == '__main__':
    s = Solution()

    assert s.isValidSudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]) is True

    assert s.isValidSudoku([
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]) is False