def printBoard(board):
    for row in board:
        print(' '.join(map(str, row)))

if __name__ == '__main__':
    board = [['▢'] * 25 for i in range (25)]
    
    board[0][0] = '■'
    printBoard(board)