import time
s_time = time.time()

grid = [[1,0,0,0,0,4,6,0,0],
        [7,0,0,0,0,3,0,0,0],
        [0,0,0,0,5,0,0,0,0],
        [0,0,0,0,4,5,0,0,0],
        [6,0,0,0,0,0,0,5,0],
        [3,0,7,1,9,0,2,0,0],
        [0,0,0,5,0,0,9,0,0],
        [0,8,0,0,2,0,0,0,3],
        [0,6,0,0,7,0,4,0,0]]

def print_board(board):
    for i in range(9):
        if i%3==0 and i!=0:
                print("---------------------")
        for j in range(9):
            if j>2 and j%3==0:
                print("|",end=" ") 
            print(board[i][j],end=" ")
        print()
        
def get_pos(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i,j
    return None

def valid_board(board,row,col):
    
    for i in range(9):
        if (row,i)!=(row,col) and board[row][i]==board[row][col]:
            return False
        else:
            continue
            
    for i in range(9):
        if (i,col)!=(row,col) and board[i][col]==board[row][col]:
            return False
        else:
            continue
    
    if row < 3:
        inside_block_row = 0
    elif row < 6:
        inside_block_row = 1
    else:
        inside_block_row = 2

    if col <3:
        inside_block_col = 0
    elif col < 6:
        inside_block_col = 1
    else:
        inside_block_col = 2
        

    inside_block_row = inside_block_row * 3
    inside_block_col = inside_block_col * 3
    
    for i in range(inside_block_row,inside_block_row+3,1):
        for j in range(inside_block_col,inside_block_col+3,1):
            if (i,j)!=(row,col) and board[i][j]==board[row][col]:
                return False
    
    return True

def solve():
    global grid
    pos = get_pos(grid)
    if not pos:
        return True
    
    row,col = pos[0],pos[1]
    for i in range(1,10,1):
        grid[row][col] = i
        if valid_board(grid,row,col):
            if solve():
                return True
        grid[row][col] = 0
    
    return False

print("Input sudoku: ")
print()
print_board(grid)
print("---------------------------------")
solve()
print("Output sudoku: ")
print()
print_board(grid)
print()

print("Executuin time : ",time.time()-s_time,'s')
