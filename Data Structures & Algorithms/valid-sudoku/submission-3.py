class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows and columns
        for y in range(9):
            row, col = set(), set()

            for x in range(9):
                if board[y][x] in row:
                    return False
                elif board[y][x] != ".":
                    row.add(board[y][x])

                if board[x][y] in col:
                    return False
                elif board[x][y] != ".":
                    col.add(board[x][y])

        # Check 3x3 squares
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                s = board[y][x:x+3] + board[y+1][x:x+3] + board[y+2][x:x+3]
                square = set()

                for n in s:
                    if n in square:
                        return False
                    elif n != ".":
                        square.add(n)

        return True
