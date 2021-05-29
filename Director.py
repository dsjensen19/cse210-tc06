from game.board import Board
from game.console import Console
from game.combination import Combination
from game.player import Player

class Director:
    """A code template for the person who directs the game. 
    This class controls the sequence of play.

    Stereotype: 
        Controller

    Attributes:
    combo (int): the combination selected for the players to guess
    keep_playing (boolean): whether or not the game continues
    name (string): the names of the players
    guess (int): the guess of the players
    hint (string): the hint generated for the player's guess.
    """

    def __init__(self):
        """The class constructor.

        """
        self.player = Player()
        self.console = Console()
        self.board = Board()
        self.combination = Combination()
        self.keep_playing = True
        self.items = {}
        self.turn = 0

    def start_game(self):
        combo = self.combination.get_combo()
        name1 = self.player.get_name(1)
        name2 = self.player.get_name(2)
        guess = "----"
        hint = "****"
        self.items = {name1 : [combo, guess, hint], name2 : [combo, guess, hint]}
        self.console.display(items)

        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.put_outputs()

    def get_inputs(self):
        
        self.player.start_turn(items[self.turn])
        self.items[self.turn][1] = self.player.get_guess()

    def do_updates(self):
        if self.items[self.turn][0] == self.items[self.turn][1]:
            self.keep_playing = False
        else:
            self.items[self.turn][2] = self.board.get_hint(self.items[self.turn][0], self.items[self.turn][1])

            if self.turn == 1:
                self.turn = 0
            else:
                self.turn = 1

    def put_outputs(self):
        if self.keep_playing == True:
            self.console.display(self.items)
        else:
            self.console.win_message(self.items[self.turn])