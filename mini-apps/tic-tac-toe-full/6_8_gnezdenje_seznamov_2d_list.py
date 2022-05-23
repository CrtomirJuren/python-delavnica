board = []

i = 0
for x in range(3):
    row = []
    for y in range(3):
        i += 1
        row.append(i)
    board.append(row)

print(board)

# indexes
"""
      columns
     0   1   2
rows 3   4   5
     6   7   8

           indexes
    [0][0] [0][1] [0][2]
    [1][0] [1][1] [1][2]
    [2][0] [2][1] [2][2]
"""

# get single cell
row = 0
column = 0
cell_0 = board[row][column]
print(cell_0)

# get two elements from row
# get single cell
cell_0 = board[0][0:2]
print(cell_0)

# get single rows
# row_1 = board[0] # 1,2,3
# print(row_1)

# # get columns
# row_1 = [board[0][0],board[0][1],board[0][0]] # 1,2,3
# print(row_1)