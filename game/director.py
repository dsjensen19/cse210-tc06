from game.board import Board
import game.console as console
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

        self.player_1 = Player()
        self.player_2 = Player()
        self.player_1.name = console.propmt_player_name(1)
        self.player_2.name = console.propmt_player_name(2)
        self.players = [self.player_1, self.player_2]
        self.num_players = len(self.players)

        
        self.combination = Combination()
        self.board = Board(self.combination.combination)

        self.guesses = []
        self.keep_playing = True
        self.turn = 0

    def start_game(self):
        self.put_outputs(None)
        while self.keep_playing:

            player_index = self.turn % self.num_players
            player = self.players[player_index]
            self.get_inputs(player)
            self.do_updates(player)
            self.put_outputs(player)
            
            

    def get_inputs(self, player):
        player.make_guess(self.guesses)


    def do_updates(self, player):
        self.guesses.append(player.guess)
        if self.combination.combination in self.guesses:
            self.keep_playing = False
        else:
            player.hint = self.board.get_hint(player.guess)
        self.turn +=1

    def put_outputs(self, player):
        print(self.combination.combination)
        if self.keep_playing == True:
            console.print_players(self.players)
        else:
            print(f"{player.name} won!")