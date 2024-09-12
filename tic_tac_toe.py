class TicTacToe:
    def __init__(self):
        # Initialize the board as a 3x3 grid of empty strings
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def display_board(self):
        # Display the board with row and column separation
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def make_move(self, row, col):
        # If the cell is empty, make the move
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            return True
        return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                return self.board[row][0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_board_full(self):
        # Check if all the cells are filled
        for row in self.board:
            if " " in row:
                return False
        return True

    def switch_player(self):
        # Toggle between player X and O
        self.current_player = "O" if self.current_player == "X" else "X"

    def play_game(self):
        # Main game loop
        print("Tic-Tac-Toe Game!")
        self.display_board()

        while True:
            row, col = map(int, input(f"Player {self.current_player}, enter your move (row and column): ").split())
            
            if 0 <= row < 3 and 0 <= col < 3 and self.make_move(row, col):
                self.display_board()
                
                winner = self.check_winner()
                if winner:
                    print(f"Player {winner} wins!")
                    break
                elif self.is_board_full():
                    print("The game is a tie!")
                    break
                else:
                    self.switch_player()
            else:
                print("Invalid move. Please try again.")

# Create a game instance and start playing
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
