import random

def setTurn():
    if random.random() >= 0.5:
        return 0
    else: return 1

if __name__ == '__main__':
    class ticTacToe:
            def __init__(self, turn):
                self.board = [['-'] * 3 for i in range (3)]
                self.val = [['0'] * 3 for i in range (3)]
                self.turn = turn
                self.playing = True
                while self.playing:
                    if self.turn == 0:
                        ticTacToe.printBoard(self)
                        if ticTacToe.checkWinner(self) == 0:
                            continue
                        ticTacToe.checkMov(self)
                        print('Es tu turno, elija la fila donde desea insertar la X')
                        try:
                            row = int(input()) - 1
                        except: 
                            print('Valor no soportado')
                            break
                        print ('Elija la fila')
                        try:
                            colum = int(input()) - 1
                        except: 
                            print('Valor no soportado')
                            break
                        if colum < 4 and row < 4 and self.board[row][colum]:
                            self.board[row][colum] = 'X'
                            self.turn = 1
                        else:
                            print('Casilla ocupada o filas y columnas fuera de rango')
                            continue
                        ticTacToe.checkWinner(self)
                    if self.turn == 1:
                        ticTacToe.checkMov(self)
                        bestOption = ticTacToe.canWin(self)
                        if len(bestOption) > 1:
                                self.board[bestOption[0]][bestOption[1]] = 'O'
                                self.turn = 0
                        else:
                            row = random.randint(0,2)
                            colum = random.randint(0,2)
                            if self.board[row][colum] == '-':
                                self.board[row][colum] = 'O'
                                self.turn = 0

            def printBoard(self):
                for row in self.board:
                    print(' '.join(map(str, row)))
            
            def checkWinner(self):
                if self.board[0][0] == 'X' and self.board[0][1] == 'X' and self.board[0][2] == 'X':
                    print ('Tu ganas')
                    self.playing = False
                    return 0
                if self.board[1][0] == 'X' and self.board[1][1] == 'X' and self.board[1][2] == 'X':
                    print ('Tu ganas')
                    self.playing = False
                    return 0
                if self.board[2][0] == 'X' and self.board[2][1] == 'X' and self.board[2][2] == 'X':
                    print ('Tu ganas')
                    self.playing = False
                    return 0
                if self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X':
                    print ('Tu ganas')
                    self.playing = False
                    return 0
                if self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X':
                    print ('Tu ganas')
                    self.playing = False
                    return 0
                if self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X':
                    print ('Tu ganas')
                    self.playing = False
                    return 0
                if self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X':
                    print ('Tu ganas')
                    self.playing = False
                    return 0
                if self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X':
                    print ('Tu ganas')
                    self.playing = False
                    return 0
                
                if self.board[0][0] == 'O' and self.board[0][1] == 'O' and self.board[0][2] == 'O':
                    print ('PC gana')
                    self.playing = False
                    return 0
                if self.board[1][0] == 'O' and self.board[1][1] == 'O' and self.board[1][2] == 'O':
                    print ('PC gana')
                    self.playing = False
                    return 0
                if self.board[2][0] == 'O' and self.board[2][1] == 'O' and self.board[2][2] == 'O':
                    print ('PC gana')
                    self.playing = False
                    return 0
                if self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O':
                    print ('PC gana')
                    self.playing = False
                    return 0
                if self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O':
                    print ('PC gana')
                    self.playing = False
                    return 0
                if self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O':
                    print ('PC gana')
                    self.playing = False
                    return 0
                if self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O':
                    print ('PC gana')
                    self.playing = False
                    return 0
                if self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O':
                    print ('PC gana')
                    self.playing = False
                    return 0

            def checkMov(self):
                if not '-' in self.board[0] and not '-' in self.board[1] and not '-' in self.board[2]:
                    print('Partida sin movimientos')
                    self.playing = False

            def canWin(self):
                for row in range (3):
                    for i in range (3):
                        if self.board[row][i] == 'X':
                            self.val[row][i] = 1
                        if self.board[row][i] == '-':
                            self.val[row][i] = 0
                        if self.board[row][i] == 'O':
                            self.val[row][i] = -2
                
                for row in range (3):
                    if self.val[row][0] + self.val[row][1] + self.val[row][2] == 2 or self.val[row][0] + self.val[row][1] + self.val[row][2] == -4:
                        if self.val[row][0] == 0:
                            colum = 0
                        if self.val[row][1] == 0:
                            colum = 1
                        if self.val[row][2] == 0:
                            colum = 2
                        return [row, colum]
                
                for colum in range (3):
                    if self.val[0][colum] + self.val[1][colum] + self.val[2][colum] == 2 or self.val[0][colum] + self.val[1][colum] + self.val[2][colum] == -4:
                        if self.val[0][colum] == 0:
                            row = 0
                        if self.val[1][colum] == 0:
                            row = 1
                        if self.val[2][colum] == 0:
                            row = 2
                        return [row, colum]
                    
                if self.val[0][0] + self.val[1][1] + self.val[2][2] == 2 or self.val[0][0] + self.val[1][1] + self.val[2][2] == -4:
                    if self.val[0][0] == 0:
                        row = 0
                        colum = 0
                    if self.val[1][1] == 0:
                        row = 1
                        colum = 1
                    if self.val[2][2] == 0:
                        row = 2
                        colum = 2
                    return [row, colum]
                
                if self.val[0][2] + self.val[1][1] + self.val[2][0] == 2 or self.val[0][2] + self.val[1][1] + self.val[2][0] == -4:
                    if self.val[0][2] == 0:
                        row = 0
                        colum = 2
                    if self.val[1][1] == 0:
                        row = 1
                        colum = 1
                    if self.val[2][0] == 0:
                        row = 2
                        colum = 0
                    return [row, colum]
                
                return {0}
                
    play = ticTacToe(setTurn())