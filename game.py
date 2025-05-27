from board import Board
from player import Player
from constants import BLACK, WHITE
import re

class Game:

    def __init__(self):
        self.player1 = Player(BLACK)
        self.player2 = Player(WHITE)
        self.board = Board()
    
    # NB: game_end, draw_board and MakeMove are not ready
    def run(self):
        """Run the game
        """
        while not self.game_end():
            # if player 1 has some possible moves, starting its turn
            if not len(self.board.list_legal_moves(BLACK)) == 0:
                # first, draw the board
                print("---- Player 1 (black) turn ----")
                print(self.board.draw_board())

                # then, start the player 1 turn 
                # we ask player 1 to choose a move
                player1_move_str = self.player1.play("Your move: ").lower()

                # while makemove is false (i.e., illegal move), asks again the player
                while (not self.check_move_regex(player1_move_str) or not self.board.make_move(self.player1.color, self.str_to_coord(player1_move_str))):
                    print('Invalid move. Try again!')
                    player1_move_str = self.player1.play("Your move: ").lower()
                    
            # if player 2 has some possible moves, starting its turn
            if not len(self.board.list_legal_moves(WHITE)) == 0:
                # once the move is accepted and the changes on the board are done,
                # we print the updated board
                print("---- Player 2 (white) turn ----")
                print(self.board.draw_board())

                # then, start the player 2 turn
                # we ask player 2 to choose a move
                player2_move_str = self.player2.play("Your move: ").lower()

                # while makemove is false (i.e., illegal move), asks again the player
                while (not self.check_move_regex(player2_move_str) or not self.board.make_move(self.player2.color, self.str_to_coord(player2_move_str))):
                    print('Invalid move. Try again!')
                    player2_move_str = self.player2.play("Your move: ").lower()

            # end of the turn, we loop back (if the game_end is not true)
        # if game_end is true, we print the scores
        print("End of the game")
        print("Player 1 (black) score: ", self.board.score()["Black "])
        print("Player 2 (white) score: ", self.board.score()["White "])

    @staticmethod
    def str_to_coord(move_str: str) -> tuple:
        """Converts the move from an str format (user format) into a tuple format (program format)

        Args:
            move_str (str): user input

        Returns:
            tuple: column number, line number
        """
        move_letter = move_str[0:1]
        move_int = int(move_str[1:2]) - 1
        dict_convert = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7
        }
        return move_int, dict_convert[move_letter]
    
    @staticmethod
    def check_move_regex(move_str: str) -> bool:
        """checks if the move is a valid coordinate (a-h and 1-8)

        Args:
            move_str (str): the string of the user input

        Returns:
            bool: True if valid, False otherwise
        """
        return re.match(r"^[a-h][1-8]$", move_str)

    # maybe this function should be in the Board class
    # def flip_list(list_to_flip):
    #     # for each element of the list, execute the flip method
    #     for i in list_to_flip:
    #         pawn.flip()
    
    # def possible_moves(self) -> tuple:
    #     """checks whether there are possible moves for each player

    #     Returns:
    #         tuple: None, None if there are no possible moves anymore
    #     """
    #     # for each square of the board grid, check if there would be a legal
    #     # move on this square and 
    #     player1_possible_moves = None
    #     player2_possible_moves = None
    #     for square in self.board.grid:
    #         if isinstance(self.board.list_legal_moves(self.player1.color, square), list):
    #             player1_possible_moves = self.board.list_legal_moves(self.player1.color, square)
    #         if isinstance(self.board.list_legal_moves(self.player2.color, square), list):
    #             player2_possible_moves = self.board.list_legal_moves(self.player2.color, square)
    #     return player1_possible_moves, player2_possible_moves

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
    print("str_to_coord: ", Game.str_to_coord("C4") == (2, 3))