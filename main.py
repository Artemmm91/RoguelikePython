from sys import exit
from game_files.main_game import MainGame

if __name__ == "__main__":
    this_game = MainGame()
    this_game.main_loop()
    exit()
