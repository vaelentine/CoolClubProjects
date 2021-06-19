""" 
Diceroller
"""
import random


class Die(object):
	def __init__(self, sides = 6):
		self.sides = sides

	def roll(self):
		return random.randint(1, self.sides)

if __name__ == '__main__':
	d6 = Die(6)
	roll_list = []
	for roll in range(0, 100):
		roll_list.append(d6.roll())


	print(f'100 d6 rolls: {roll_list}')