
class Board():
    def __init__(self):
        pass
    """seperates 4digit intager into a length 4 array od 1digit intagers"""
    def code_to_list(self, code):
        list = [0, 0, 0, 0]

        list[3] = code % 10
        code //= 10
        list[2] = code % 10
        code //= 10
        list[1] = code % 10
        list[0] = code // 10
        return list
    def get_hint(self, code, guess):
        code = self.code_to_list(code)
        guess = self.code_to_list(guess)

        x = 0
        o = 0

        """ if there are same numbers in the corect position, and adds one to x and changes those numbers to -1"""
        for i in range(4):
            if code[i] == guess[i]:
                x += 1
                code[i] = guess[i] = -1

        """fancy way of removing the -1 from the list"""
        guess = [x for x in guess if x > -1]
        code  = [x for x in code  if x > -1]

        """ if there are same numbers in incorect positions, and adds one to 0 and removes the nember from code so it can not be counted twice"""
        for digit in guess:
            if digit in code:
                o += 1
                code.remove(digit)
        
        put_x    = f"{   '':x<{x}}"
        put_o    = f"{put_x:o<{x+o}}"
        put_star = f"{put_o:*<4}"
        return put_star