from random import randint

class Die:
    '''a class representing a single die'''

    def __init__(self, num_sides=6):
        '''asume a six sided Die'''
        self.num_sides = num_sides


    def roll(self):
        '''return a random between 1 and num_sides'''
        return randint(1, self.num_sides)