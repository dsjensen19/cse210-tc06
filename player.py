"""
PLAYER()
   
   get_name:
      input name statement
      return name
   start_turn(name):
      print "Player {name}'s turn"
   get_guess():
      return response to "what is your guess?"
      """
class Player():
    def __init__(self):
        self.name = "Player1"
        self.names = []
        self.guesses = []

    def get_name(self):
        #Print previous guesses?
        name = str(input("Guess your number 1000-9999! "))
        while len(guess) != 1 or guess in self.guesses:
            guess = input("Guess your number 1000-9999! ")
        self.name = name
        self.names.append(name)
        return name
    def get_guess(self):
        #Print previous guesses?
        guess = input("Guess your number 1000-9999! ")
        while guess <1000 or guess >9999 or guess in self.guesses:
            guess = input("Guess your number 1000-9999! ")
        self.guesses.append(guess)  
        return guess