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
import unittest


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
        if not isinstance(d_string, str):
            raise TypeError("Argument type must be a string")
        check_exp = match(r'^([1-9][0-9]*)d([1-9][0-9]*)$', d_string)
        if check_exp:
            number = int(check_exp.group(1))
            sides = int(check_exp.group(2))
            self.roll_xy(number, sides)
        else:
            raise ValueError("String must be in form of 'xdy', where x and y positive nonzero integers")


class TestFunction(unittest.TestCase):
    def setUp(self):
        self.dice = Dice()
        self.val_error_string = "String must be in form of 'xdy', where x and y positive nonzero integers"
        self.typ_error_string = "Argument type must be a string"

    def test1_roll_zero_dice(self):
        with self.assertRaises(ValueError) as context:
            self.dice.roll('0d4')
        self.assertTrue(self.val_error_string in str(context.exception))

    def test2_roll_invalid_text(self):
        with self.assertRaises(ValueError) as context:
            self.dice.roll('2b6')
        self.assertTrue(self.val_error_string in str(
            context.exception))

    def test3_roll_zero_sided_die(self):
        with self.assertRaises(ValueError) as context:
            self.dice.roll('2d0')
        self.assertTrue(self.val_error_string in str(
            context.exception))

    def test4_roll_negative_number(self):
        with self.assertRaises(ValueError) as context:
            self.dice.roll('-2d20')
        self.assertTrue(self.val_error_string in str(
            context.exception))

    def test5_roll_list_has_correct_number_of_items(self):
        self.dice.roll('20d6')
        self.assertEqual(len(self.dice.rolls), 20)

    def test6_previous_roll_is_correctly_stored(self):
        self.dice.roll('30d5')
        total1 = self.dice.total
        self.dice.roll('10d8')
        self.assertEqual(total1, self.dice.previous_total)

    def test7_none_type_type_error_handled(self):
        with self.assertRaises(TypeError) as context:
            self.dice.roll(None)
        self.assertTrue(self.typ_error_string in str(
            context.exception))

    def test8_object_type_type_error_handled(self):
        with self.assertRaises(TypeError) as context:
            self.dice.roll(None)
        self.assertTrue(self.typ_error_string in str(
            context.exception))


if __name__ == '__main__':
    unittest.main()