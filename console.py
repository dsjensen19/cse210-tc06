from game.board import Board
from game.combination import Combination
from game.player import Player

class Console():
    def __init__(self):
        """The class constructor.
        """
        self.player = Player()
        self.console = Console()
        self.board = Board()

    def print_dashes():
    #prints a line of dashes for displaly
        print()
        print('_________________________________')
        
    def print_info(self):
    #prints out a name, their guess, and the hint
        print("Player, " + self.Player.name + "has guessed " + self.Player.guess + ". Their hint is, " + self.Board.get_hint + ".")