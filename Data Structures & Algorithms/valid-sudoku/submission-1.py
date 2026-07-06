class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[[set()for _ in range(3)]for _ in range(9)]
        
        for x in range(9):
            for y in range(9):
                if board[x][y]==".":
                    continue
                if board[x][y] in rows[x]:
                    return False
                else:
                    rows[x].add(board[x][y])
                if board[x][y] in cols[y]:
                    return False
                else:
                    cols[y].add(board[x][y])    
                if board[x][y] in box[x//3][y//3]:
                    return False
                else:
                    box[x//3][y//3].add(board[x][y])
        return True