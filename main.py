import random

class TicTacToe:
    player1_vic = 0
    player2_vic = 0
    board = [['-' for _ in range(3)] for _ in range(3)]
    
    def main(self):
        player_1 = input("Type name of the first player: ")
        player_2 = input("Type name of the second player: ")
        self.show_board()
        self.play()

    def play(self):
        current_player = random.randint(1, 2)
        if current_player == 1:
            print("Player 1 starts symbol -> X")
        else:
            print("Player 2 starts symbol -> O")
        
        while True:
            row = int(input("Type row to mark: "))
            col = int(input("Type column to mark: "))
            self.make_move(row, col, current_player)
            
            if self.check_winner(current_player):
                if current_player == 1:
                    print("Player 1 wins!")
                    self.player1_vic += 1
                else:
                    print("Player 2 wins!")
                    self.player2_vic += 1
                break
            
            current_player = 3 - current_player

    def show_board(self):
        for row in self.board:
            print(' '.join(row))

    def check_winner(self,player):
        symbol = 'X' if player == 1 else 'O'
                
        return False
    def make_move(self,row,col,player):
        if(self.board[row][col]=="-"):
            if(player==1):
                self.board[row][col]='X'
            else:
                self.board[row][col]='0'

        else:
            print("Esa posicion ya esta marcada!")
        self.show_board()

    def show_stats(self):
        print("Victories of player 1: " + str(self.player1_vic))
        print("Victories of player 2: " + str(self.player2_vic))

if __name__ == "__main__":
    game = TicTacToe()
    game.main()
