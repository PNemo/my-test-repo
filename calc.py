from random import randint

class Dice:
    """Rolls a dice"""
    def __init__(self, sides):
        self.sides = sides
    
    def roll_dice(self):
        roll = randint(1, self.sides)
        print(f'Rolling a dice, you have got: ')
        print(roll)

dice1 = Dice(10)
dice2 = Dice(20)
dice1.roll_dice()
dice2.roll_dice()