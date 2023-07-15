def main():
    board=[" "for x in range(9)]
    player_1=input("Type name of the first player: ")
    player_2=input("Type name of the second player: ")
    show_board(board)

def show_board(board):
    print ( "   |   |   ")
    print (" "+board[0]+" | "+board[1]+" | "+board[2]+"  ")
    print ("   |   |")
    print ("---|---|---")
    print (" "+board[3]+" | "+board[4]+" | "+board[5]+"  ")
    print ("   |   |")
    print ("---|---|---")
    print (" "+board[6]+" | "+board[7]+" | "+board[8]+"  ")
    print ("   |   |   ")



if __name__ == "__main__":
    main()
