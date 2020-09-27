"""
Get the middle character
From codewars
https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character.
If the word's length is even, return the middle 2 characters.
#Examples:
Kata.getMiddle("test") should return "es"
Kata.getMiddle("testing") should return "t"
Kata.getMiddle("middle") should return "dd"
Kata.getMiddle("A") should return "A"
"""
# unit test case
import unittest

def get_middle(s):
    # if length of word % 2 == 0, you'd return index 1 & 2
    #middle character of dog, len 3, would be 1.
        return s[len(s)/2-1:len(s)//2+1] if len(s) % 2 == 0 else s[len(s)/2]

print(get_middle(""))

class TestFunction(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_middle("test"), "es")
    def test2(self):
        self.assertEqual(get_middle("testing"), "t")
    def test3(self):
        self.assertEqual(get_middle("middle"), "dd")
    def test4(self):
        self.assertEqual(get_middle("A"), "A")
    def test5(self):
        self.assertEqual(get_middle("of"), "of")

if __name__ == '__main__':
    unittest.main()



