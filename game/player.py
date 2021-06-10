class Player():
    def __init__(self):
        self.name = "Player1"
        #(unused code)self.names = []
        self.guesses = []

    def get_name(self):
        #Print previous guesses?
        name = str(input("Please enter a name for your player: "))
        self.name = name
        #(unused code)self.names.append(name)
        #return name
    def get_guess(self):
        #Print previous guesses?
        print(self.name + "'s turn!")
        guess = input("Guess your number 1000-9999! ")
        while guess <1000 or guess >9999 or guess in self.guesses:
            if guess < 1000:
                print("To small, enter a 4 digit number please.")
                guess = input("Guess your number 1000-9999! ")
            elif guess > 9999:
                print("To large, enter a 4 digit number please.")
                guess = input("Guess your number 1000-9999! ")
            elif guess in self.guesses:
                print("You already guessed that!")
                guess = input("Guess your number 1000-9999! ")
        self.guesses.append(guess)  
        return guess