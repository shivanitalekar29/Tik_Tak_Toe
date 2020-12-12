board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player: str = "X"
game_is_playing: bool = True
winner = None


class Display:
    def display_board(self):
        print(board[0] + " | " + board[1] + " | " + board[2])
        print(board[3] + " | " + board[4] + " | " + board[5])
        print(board[6] + " | " + board[7] + " | " + board[8])


class Handleturn(Display):
    def handle_turn(self):

            position = int(input("Enter the position from 0 to 8:"))  # 5
            board[position] = current_player


class Swapplayers(Handleturn):
    def swap_player(self):
        global current_player
        if current_player == "X":  # "o"=="X"
            current_player = "O"
        elif current_player == "O":  # "O"=="O"
            current_player = "X"


class Checkthewinner(Swapplayers):
    def check_the_winner(self):
        # check row
        # check col
        # check dia
        global winner
        row_winner = self.check_row()
        if row_winner:
            winner = row_winner

        col_winner = self.check_col()
        if col_winner:
            winner = col_winner

        dia_winner = self.check_dia()
        if dia_winner:
            winner = dia_winner

    def check_row(self):
        global game_is_playing
        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"

        if row_1 or row_2 or row_3:
            game_is_playing = False

        if row_1:
            return board[2]
        elif row_2:
            return board[4]
        elif row_3:
            return board[6]

    def check_col(self):
        global game_is_playing
        col_1 = board[0] == board[3] == board[6] != "-"
        col_2 = board[1] == board[4] == board[7] != "-"
        col_3 = board[2] == board[5] == board[8] != "-"

        if col_1 or col_2 or col_3:
            game_is_playing = False

        if col_1:
            return board[0]
        elif col_2:
            return board[1]
        elif col_3:
            return board[5]

    def check_dia(self):
        global game_is_playing
        dia_1 = board[0] == board[4] == board[8] != "-"
        dia_2 = board[2] == board[4] == board[6] != "-"

        if dia_1 or dia_2:
            game_is_playing = False

        if dia_1:
            return board[0]
        elif dia_2:
            return board[4]

    def check_tie(self):
        global game_is_playing
        if "-" not in board:
            print("Match is tied")
            game_is_playing = False


class Playgame(Checkthewinner):
    def __init__(self):
        while game_is_playing:  # while False:
            self.display_board()
            self.handle_turn()
            self.swap_player()
            self.check_the_winner()
            self.check_tie()

        global winner
        if winner == "X" or winner == "O":
            self.display_board()
            print("winner is", winner)


p = Playgame()
