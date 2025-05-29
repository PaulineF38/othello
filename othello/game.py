from .board import Board
from .humanplayer import HumanPlayer
from .player import Player
from .airandom import AIRandom
from .constants import BLACK, WHITE, BLACK_STR, WHITE_STR, QUIT_STR, MODE_HVSH, MODE_HVSM, MODE_HVSR, MODE_RVSM
from .aiplayermax import AIPlayerMax
import re

class Game:

    def __init__(self):
        self.board = Board(*(Player.ask_board()))
        mode = Player.ask_mode()
        if mode == MODE_HVSH :
            self.player1 = HumanPlayer(BLACK)
            self.player2 = HumanPlayer(WHITE)
        elif mode == MODE_HVSM:
            self.player1 = HumanPlayer(BLACK)
            self.player2 = AIPlayerMax(WHITE)
        elif mode == MODE_HVSR:
            self.player1 = HumanPlayer(BLACK)
            self.player2 = AIRandom(WHITE)
        elif mode == MODE_RVSM:
            self.player1 = AIRandom(BLACK)
            self.player2 = AIPlayerMax(WHITE)
    
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
        print(" ---      Winner      ---")
        print(self.winner())



    @staticmethod
    def str_to_coord(move_str: str) -> tuple:
        """Converts the move from a str format (user format) into a tuple format (program format)

        Args:
            move_str (str): user input

        Returns:
            tuple: column number, line number
        """
        if move_str[0].isalpha() :
            move_letter = move_str[0]
            move_int = int(move_str[1:]) - 1
        else :
            move_letter = move_str[-1]
            move_int = int(move_str[:-1]) - 1
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
    def coord_to_str(i, j) -> str:
        """Converte 1,1 to B1

        Args:
            i (int): number of the row
            j (int): number of the column

        Returns:
            str: string of the convert coordinate
        """     
        # use chr to convert a b c ... in number   
        letter = chr(ord('a') + j).upper()
        number = i + 1 
        return f"{letter}{number}"
    
    def prompt_player(self, player: Player)-> str:
        """Displays the possible moves for the given player and prompts for their input.

        Args:
            player (Player):  The player object
        Returns:
            str: The string entered by the player, converted to lowercase
        """      
        # Creat the liste of the possible move with convert coordinates (i.e. B1 ans not 1,1)  
        converted = [Game.coord_to_str(*coords) for coords in self.board.list_legal_moves(player.color)]
        print(f"possible moves : {converted}")
        # Ask the player for their move input
        move_str = player.play("Your move (give a coordinate (ex: C2) or Quit): ", self.board).lower()
        return move_str

    def check_move_regex(self, move_str: str) -> bool:
        """checks if the move is a valid coordinate

        Args:
            move_str (str): the string of the user input

        Returns:
            bool: True if valid, False otherwise
        """
        n_rows = self.board.grid_shape()[0]
        n_cols = self.board.grid_shape()[1]
        end_digit = str(n_rows%10)
        end_letter = chr(96+n_cols)

        # Regex with group to search "B52"-like or "52B"-like strings
        m = re.match(rf'(?P<letter_number>^[A-Za-z](?:[1-9][0-9]?|100)$)|(?P<number_letter>^(?:[1-9][0-9]?|100)[A-Za-z]$)', move_str)

        if m is not None : # There is a match !
            if m.groupdict()["letter_number"] is not None : # Match smthg like B52
                letter = move_str[0].lower()
                number = int(move_str[1:])
            elif m.groupdict()["number_letter"] is not None : # Match smthg like 52B
                letter = move_str[-1].lower()
                number = int(move_str[:-1])
            else :
                raise RuntimeError("This should not have been reached ...")
            move_is_ok = (letter <= end_letter and number <= n_rows)
        else : # There is no match !
            move_is_ok = False

        return move_is_ok

    def game_end(self) -> bool:
        """checks whether the game should be ended, because no possible moves

        Returns:
            bool: True if the game should be ended, False otherwise
        """
        if len(self.board.list_legal_moves(BLACK)) == 0 and len(self.board.list_legal_moves(WHITE)) == 0:
            return True
        else:
            return False

    def winner(self) -> str:
        """checks who is the winner

        Returns:
            the name of player
        """
        if self.board.score()["Black "] > self.board.score()["White "]:
            return f"Congradulation !! you are THE WINNER {self.player1.name}\nBOOOOOOOOH!! you are THE LOSER {self.player2.name}"
        elif self.board.score()["Black "] == self.board.score()["White "]:
            return f"Both are equal"
        else:
            return f"Congradulation !! you are THE WINNER {self.player2.name}\nBOOOOOOOOH!! you are THE LOSER {self.player1.name}"
        
        