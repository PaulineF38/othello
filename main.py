#!/usr/bin/env python3

from othello.game import Game

try :
    # Create a game ...
    game = Game()

    # ... and run it
    game.run()
except KeyboardInterrupt :
    print("")
    print("-------------------------------")
    print(" - Ok ciao ! See you later ! - ")
    print("-------------------------------")

