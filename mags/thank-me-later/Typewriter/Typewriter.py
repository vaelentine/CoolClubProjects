import pygame
from colorama import init, Fore, Style
from time import sleep
from os import system, name
import sys
from random import choice

# prints whatever text onto screen with a blip sound and a delay
class Typewriter:
    def __init__(self):
        pygame.mixer.init()

        self.speed = 20
        self.color = "white"
        self.volume =0.02
        self.sound = pygame.mixer.Sound("blip_01.wav")

    def type_key(self, char):
        self.sound.set_volume(self.volume)
        print(char, end="")
        sys.stdout.flush()
        pygame.mixer.Sound.play(self.sound)

    def clear(self):
        # windows
        if name == 'nt':
            _ = system('cls')
        # for unix based
        else:
            _ = system('clear')
        # add some extra padding
        print(end='\n\n')

    def print(self, text):
        for char in text:
            self.type_key(char)
            sleep(1/self.speed)
        print(end='\n\n')



if __name__ == "__main__":
    t = Typewriter()
    t.print("""This is a test script. \nIf you are reading this, you are running this directly.""")