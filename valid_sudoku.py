import re

# board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"],
# ]

board = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".",".",".",".",".","."],
    ["5",".",".",".",".",".",".","9","."],
    [".",".",".","5","6",".",".",".","."],
    ["4",".","3",".",".",".",".",".","1"],
    [".",".",".","7",".",".",".",".","."],
    [".",".",".","5",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]

def validSudoku(board):
    def dupes(iter_obj):
        regex = re.compile(r'\d+')
        all_nums = regex.findall(str(iter_obj))
        nd_nums = set(all_nums)
        return len(all_nums) == len(nd_nums)

    def squares_valid(board):
        for x in range(0, 9, 3):
            y = x + 3
            for i in range(0, 9, 3):
                j = i + 3
                square = [item[i:j] for item in board[x:y]]
                if not dupes(square):
                    return False
        return True
    
    def cr_valid(board):
        for x in range(0, 9):
            row = [item for item in board[x]]
            column = [item[x] for item in board]
            if not dupes(column) or not dupes(row):
                return False
        return True
    
    if cr_valid(board) and squares_valid(board):
        return True
    return False

print(validSudoku(board))