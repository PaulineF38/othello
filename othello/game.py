from .board import Board
from .humanplayer import HumanPlayer
from .player import Player
from .constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR
from .aiplayermax import AIPlayerMax
import re

class Game:

    def __init__(self):
        self.board = Board(*(Player.ask_board()))
        self.player1 = HumanPlayer(BLACK)
        self.player2 = HumanPlayer(WHITE)
    
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
                player1_move_str = self.prompt_player(self.player1)
                player_1_quit = (player1_move_str == QUIT_STR.lower())

                # while makemove is false (i.e., illegal move), asks again the player
                #add precise message why move is invalide

                while (not player_1_quit ):
                    # Check if the coordinate given are on board
                    if not self.check_move_regex(player1_move_str):
                        print("Invalid move: enter a valid on-board coordinate like 'C4' or 'c4'.")
                        player1_move_str = self.prompt_player(self.player1)
                        player_1_quit = (player1_move_str == QUIT_STR.lower())

                    else:
                        i, j = self.str_to_coord(player1_move_str)
                        # Invalide move = player is trying to put a pawn in not empty square
                        if not self.board.grid[i][j].empty_square():
                            print("Invalid move: the square is already occupied.")
                            player1_move_str = self.prompt_player(self.player1)
                            player_1_quit = (player1_move_str == QUIT_STR.lower())

                        # Invalide move = No pawn around
                        elif not self.board._adjacent(i, j):
                            print("Invalid move: the square is not adjacent to any opponent pawn.")
                            player1_move_str = self.prompt_player(self.player1)
                            player_1_quit = (player1_move_str == QUIT_STR.lower())

                        # invalide move = no pawn capture
                        elif len(self.board._capture(self.player1.color, i, j)) == 0:
                            print("Invalid move: no opponent pawn can be captured from this position.")
                            player1_move_str = self.prompt_player(self.player1)
                            player_1_quit = (player1_move_str == QUIT_STR.lower())

                        else:
                            # Valid move, break out of loop
                            self.board.make_move(self.player1.color, (i, j))
                            break
                        
            # if player 2 has some possible moves, starting its turn
            if not player_1_quit and not len(self.board.list_legal_moves(WHITE)) == 0:
                # once the move is accepted and the changes on the board are done,
                # we print the updated board
                print(f"---- {self.player2.name} : your turn ! (player 2 : {WHITE_STR}) ----")
                print(self.board.draw_board())

                # then, start the player 2 turn
                # we ask player 2 to choose a move
                player2_move_str = self.prompt_player(self.player2)
                player_2_quit = (player2_move_str == QUIT_STR.lower())


                # while makemove is false (i.e., illegal move), asks again the player
                while (not player_2_quit ):
                    # Check if the coordinate given are on board
                    if not self.check_move_regex(player2_move_str):
                        print("Invalid move: enter a valid on-board coordinate like 'C4' or 'c4'.")
                        player2_move_str = self.prompt_player(self.player2)
                        player_2_quit = (player2_move_str == QUIT_STR.lower())
                    else:
                        i, j = self.str_to_coord(player2_move_str)
                        # Invalide move = player is trying to put a pawn in not empty square
                        if not self.board.grid[i][j].empty_square():
                            print("Invalid move: the square is already occupied.")
                            player2_move_str = self.prompt_player(self.player2)
                            player_2_quit = (player2_move_str == QUIT_STR.lower())
                         # Invalide move = No pawn around
                        elif not self.board._adjacent(i, j):
                            print("Invalid move: the square is not adjacent to any opponent pawn.")
                            player2_move_str = self.prompt_player(self.player2)
                            player_2_quit = (player2_move_str == QUIT_STR.lower())
                        # invalide move = no pawn capture
                        elif len(self.board._capture(self.player2.color, i, j)) == 0:
                            print("Invalid move: no opponent pawn can be captured from this position.")
                            player2_move_str = self.prompt_player(self.player2)
                            player_2_quit = (player2_move_str == QUIT_STR.lower())
                        else:
                            # Valid move, break out of loop
                            self.board.make_move(self.player2.color, (i, j))
                            break

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
    
    @staticmethod
    def coord_to_str(i, j):
        letter = chr(ord('a') + j).upper()
        number = i + 1 
        return f"{letter}{number}"
    
    def prompt_player(self, player):
        converted = [Game.coord_to_str(*coords) for coords in self.board.list_legal_moves(player.color)]
        print(f"possible moves : {converted}")
        move_str = player.play("Your move (give a coordinate (ex: C2) or Quit): ", self.board).lower()
        return move_str

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
