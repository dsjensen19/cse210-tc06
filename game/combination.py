import random


"""This program creates and stores the corect combination for the mastermind game"""
class Combination():
    def __init__(self):
        self.combpnation = 0
    def get_code(self):
        self.combination = random.randint(1000, 9999)
        return self.combination
