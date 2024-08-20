n = 28

board=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(0)
    board.append(a)

def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print()
        
        
def isSafe(board,row, col):
    # column check
    n = len(board)
    for i in range(n):
        if board[row][i]==1:
            return False
    
    # row check
    for i in range(n):
        if board[i][col]==1:
            return False
    
    # diagonal check
    i = row 
    j = col
    while i<n and j<n:
        if board[i][j]==1:
            return False
        i+=1
        j+=1
        
    i = row 
    j = col
    while i>0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    i = row 
    j = col
    while i<n and j>0:
        if board[i][j]==1:
            return False
        i+=1
        j-=1
    i = row 
    j = col
    while i>0 and j>0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    
    return True


def placeQueen(board,row=0):
    if row>=len(board):
        return True
    
    for i in range(len(board)):  
        if isSafe(board,row,i):
            board[row][i] = 1
            if placeQueen(board,row+1):
                return True
            board[row][i] = 0
    
    return False

print(board)
printBoard(board)
placeQueen(board)
print("\n\n\n")
printBoard(board)