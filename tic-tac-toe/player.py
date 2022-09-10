import math 
import random

class Player:
    # we want each player to be able to pick between x and o 
    def __init__(self,letter):
        self.letter = letter 

    def get_move(slef, game):
        pass 

class ComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass