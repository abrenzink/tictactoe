

from re import X


def main():
    board = createBoard()
    player = changePlayer("")

    while not (victory(board) or draw(board)):
        displayGame(board, player)
        makeMove(player, board)
        player = changePlayer(player)
    
    displayGame(board, player)
    player = changePlayer(player)
    print("")
    print("------------------------------------------------")
    print(f"{player} is the winner! Thanks for playing.")
    print("------------------------------------------------")
    print("")

def createBoard():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def displayGame(board, player):
    print()
    print("------------------------------------------------")
    print(f"{player}'s turn to choose a square (1-9): 2")
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()
    print("------------------------------------------------")

def victory(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
    

def changePlayer(player):
    if player == "" or player == "o":
        return "x"
    elif player == "x":
        return "o"

def makeMove(player, board):
    choice = int(input(f"{player}'s turn to choose (type 1 to 9): "))
    board[choice - 1] = player

def draw(board):
    for choice in range(9):
        if board[choice] != "x" and board[choice] != "o":
            return False
    return True 

if __name__ == "__main__":
    main()
