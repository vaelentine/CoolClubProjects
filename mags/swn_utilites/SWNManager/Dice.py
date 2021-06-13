"""
Dice
A classed base dice roller:
 -roll('expression') - allows rolling in the string expression xdy, where x and y are positive nonzero integers
 -roll_xy(num, sides) - also allows the standard roll of number of dice with number of sides (default 6))
 - stores:
    - the current roll set (Dice.rolls),
    - the current total (Dice.total), and
    - the previous roll total (Dice.previous_total)
"""

from random import randint
from re import match


class Dice(object):
    def __init__(self):
        self.rolls = None
        self.total = None
        self.previous_total = None

    def _update_values(self, current_rolls):
        self.previous_total = self.total
        self.rolls = current_rolls
        self.total = sum(current_rolls)

    def roll_xy(self, number, sides=6):
        current_rolls = []
        for i in range(number):
            current_rolls.append(randint(1, sides))
        self._update_values(current_rolls)
        return self.total

    def roll(self, d_string):
        check_exp = match(r'^([1-9][0-9]*)d([1-9][0-9]*)$', d_string)
        if check_exp:
            number = int(check_exp.group(1))
            sides = int(check_exp.group(2))
            self.roll_xy(number, sides)
        else:
            raise ValueError("Roll must be a string in the form of 'xdy', where x and y positive nonzero integers")
