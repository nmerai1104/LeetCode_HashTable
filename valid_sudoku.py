class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    current = board[i][j]
                    # Check for the same value in the same row, column, or sub-box
                    if (i, current) in seen or (current, j) in seen or (i // 3, j // 3, current) in seen:
                        return False

                    seen.add((i, current))
                    seen.add((current, j))
                    seen.add((i // 3, j // 3, current))

        return True
