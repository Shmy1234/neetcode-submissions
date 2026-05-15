class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(9): 
            row, col, square = set(), set(), set()
            for x in range(9):
                if board[y][x].isdigit() and board[y][x] in row:
                    return False
                elif board[y][x].isdigit() and board[y][x] not in row:
                    row.add(board[y][x])
                
                if board[x][y].isdigit() and board[x][y] in col:
                    return False
                elif board[x][y].isdigit() and board[x][y] not in col:
                    col.add(board[x][y])

            s = board[(y//3)*3][(y%3)*3:(y%3)*3+3]\
            + board[(y//3)*3+1][(y%3)*3:(y%3)*3+3]\
            + board[(y//3)*3+2][(y%3)*3:(y%3)*3+3]

            
            for num in s:
                if num.isdigit() and num in square:
                    return False
                elif num.isdigit() and num not in square:
                    square.add(num)
        
        return True



            

        