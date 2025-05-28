from board import Board
from player import Player
from constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR
import re

class Game:

    def __init__(self):
        self.player1 = Player(BLACK)
        self.player2 = Player(WHITE)
        self.board = Board(6,8)
    
    def run(self):
        """Run the game
        """
        player_1_quit = False
        player_2_quit = False

        while not player_1_quit and not player_2_quit and not self.game_end():

            # if player 1 has some possible moves, starting its turn
            if not len(self.board.list_legal_moves(BLACK)) == 0:
                # first, draw the board
                print(f"---- {self.player1.name} : your turn ! (you are player 1 : {BLACK_STR}) ----")
                print(self.board.draw_board())

                # then, start the player 1 turn 
                # we ask player 1 to choose a move
                player1_move_str = self.player1.play("Your move (give a coordinate (ex: C2) or Quit): ").lower()
                player_1_quit = (player1_move_str == QUIT_STR.lower())

                # while makemove is false (i.e., illegal move), asks again the player
                while (not player_1_quit and (not self.check_move_regex(player1_move_str) or not self.board.make_move(self.player1.color, self.str_to_coord(player1_move_str)))):
                    print('Invalid move. Try again!')
                    player1_move_str = self.player1.play("Your move (give a coordinate (ex: C2) or Quit): ").lower()
                    player_1_quit = (player1_move_str == QUIT_STR.lower())
                    
            # if player 2 has some possible moves, starting its turn
            if not player_1_quit and not len(self.board.list_legal_moves(WHITE)) == 0:
                # once the move is accepted and the changes on the board are done,
                # we print the updated board
                print(f"---- {self.player2.name} : your turn ! (player 2 : {WHITE_STR}) ----")
                print(self.board.draw_board())

                # then, start the player 2 turn
                # we ask player 2 to choose a move
                player2_move_str = self.player2.play("Your move (give a coordinate (ex: C2) or Quit): ").lower()
                player_2_quit = (player2_move_str == QUIT_STR.lower())

                # while makemove is false (i.e., illegal move), asks again the player
                while (not player_2_quit and (not self.check_move_regex(player2_move_str) or not self.board.make_move(self.player2.color, self.str_to_coord(player2_move_str)))):
                    print('Invalid move. Try again!')
                    player2_move_str = self.player2.play("Your move (give a coordinate (ex: C2) or Quit): ").lower()
                    player_2_quit =  (player2_move_str == QUIT_STR.lower())

            # end of the turn, we loop back (if the game_end is not true)
        # if game_end is true, we print the final board and scores
        print("\n")
        if player_1_quit :
            print(f"{self.player1.name} ({BLACK_STR}) is giving up ! Shame ! Shame ! Shame !\n")
        if player_2_quit :
            print(f"{self.player2.name} ({WHITE_STR}) is giving up ! Shame ! Shame ! Shame !\n")
        print(" --- End of the game ---")
        print(self.board.draw_board())
        print(" ---      Score      ---")
        print(f"{self.player1.name} (player 1 : {BLACK_STR}) score: ", self.board.score()["Black "])
        print(f"{self.player2.name} (player 2 : {WHITE_STR}) score: ", self.board.score()["White "])

    @staticmethod
    def str_to_coord(move_str: str) -> tuple:
        """Converts the move from an str format (user format) into a tuple format (program format)

        Args:
            move_str (str): user input

        Returns:
            tuple: column number, line number
        """
        move_letter = move_str[0:1]
        move_int = int(move_str[1:]) - 1
        dict_convert = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25
        }
        return move_int, dict_convert[move_letter]
    
    # @staticmethod
    def check_move_regex(self, move_str: str) -> bool:
        """checks if the move is a valid coordinate (a-h and 1-8)

        Args:
            move_str (str): the string of the user input

        Returns:
            bool: True if valid, False otherwise
        """
        n_rows = self.board.grid_shape()[0]
        n_cols = self.board.grid_shape()[1]
        end_digit = str(n_rows%10)
        end_letter = chr(96+n_cols)
        if n_rows < 10:
            regex = bool(re.match(rf"^[a-{end_letter}][1-{end_digit}]$", move_str))
        else:
            regex = bool(re.match(rf"^[a-{end_letter}]([1-9]|1[0-{end_digit}])$", move_str))
        return regex

    def game_end(self) -> bool:
        """checks whether the game should be ended, because no possible moves

        Returns:
            bool: True if the game should be ended, False otherwise
        """
        if len(self.board.list_legal_moves(BLACK)) == 0 and len(self.board.list_legal_moves(WHITE)) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print("str_to_coord: ", Game.str_to_coord("c4") == (2, 3))