# cse210-tc06

DIRECTOR()
objects:
code
playing
name
guess
hint
items {}


start_game:
   code = get_code
   name1 = player.get_name
   name2 = player.get_name
   guess = "----"
   hint = "four asterisks"
   self.items = {name1 : [code, guess, hint], name2: [code, guess, hint]}
   get_outputs
   
   while playing
   get_inputs()
   do_updates()
   put_outputs()
   
get_inputs:
turn = 1
if turn = 1, turn = 0 and vice versa
player.start_turn(items[turn])
items[turn][1] = player.get_guess

do_updates:
items[turn][2] = board.get_hint(items[turn][0], items[turn][1])

put_outputs:
console.print_dashes
console.print_players(items)

   
CODE()

get_code:
   random number between 1000-9999
   
   
PLAYER()
   
   get_name:
      input name statement
      return name
   start_turn(name):
      print "Player {name}'s turn"
   get_guess():
      return response to "what is your guess?"
      
BOARD()
   get_hint(code, guess):
      generates hint from code and returns it
      

CONSOLE()
print_dashes:
   prints a line of dashes
print_players(dict)
   prints out a name, their guess, and the hint
      
