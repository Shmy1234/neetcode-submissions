class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # board[0][r]
        # board[c][0]
        # board[i*3][j*3]

        for y in range(len(board[0])): 
            row, col, square = set(), set(), set()
            for x in range(len(board)):
                if board[y][x] in row: 
                    return False 
                elif board[y][x] != ".": 
                    row.add(board[y][x])
                
                if board[x][y] in col: 
                    return False 
                elif board[x][y] != ".": 
                    col.add(board[x][y])
            
            s = board[(y//3)*3][(y%3)*3:(y%3)*3+3] + board[(y//3)*3+1][(y%3)*3:(y%3)*3+3] + board[(y//3)*3+2][(y%3)*3:(y%3)*3+3]

            for n in s: 
                if n in square:
                    return False
                elif n != ".":
                    square.add(n)
        
        return True
