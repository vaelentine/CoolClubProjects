from colorama import init, Fore, Style
from time import sleep
from os import system, name
import sys
from random import choice

# Colorama initialization for Windows
if name == 'nt':
    init(convert=True)

# print(f'This is {Fore.GREEN}color! {Style.RESET_ALL}')
magic_str = "  MAGIC  "
ball_str = " 8  BALL "


def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    # for unix based
    else:
        _ = system('clear')
    # add some extra padding
    print(end='\n\n')


def typewrite(string, time):
    for char in string:
        print(char, end="")
        sys.stdout.flush()
        sleep(time/len(string))

class Ball:
    outcomes = ["It is certain", "It is decidedly so.",
                "Without a doubt.",
                "Yes – definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    image = f"""
       _.a$$$$$a._
     ,$$$$$$$$$$$$$.
   ,$$$$$$$$$$$$$$$$$.
  d$$$$$$$$$$$$$$$$$$$b
 d$$$$$$$$~'-`~$$$$$$$$b
($$$$$$$p       $$$$$$$$)
$$$$$$$${magic_str}$$$$$$$$
$$$$$$$${ball_str}$$$$$$$$
($$$$$$$b       d$$$$$$$)
 q$$$$$$$$a._.a$$$$$$$$p
  q$$$$$$$$$$$$$$$$$$$p
   `$$$$$$$$$$$$$$$$$'
     `$$$$$$$$$$$$$'
       `~$$$$$$$~' """

typewrite(f' {Fore.BLUE} {Ball.image}{Style.RESET_ALL}', 3)
typewrite("\nThe Magic 8 Ball is ready to receive your question! ! ! !", 2)
sleep(1)
clear()
magicsparkles = "_.-`-." * 10
typewrite(magicsparkles,2 )

typewrite("\nType your question or just press enter when you have a yes or no question ready.", 1)
input("\n ")
sleep(1)
clear()
typewrite(magicsparkles, 2)
typewrite("\nThe Magic 8 ball has received your question.", 1)
sleep(1)
clear()
typewrite(magicsparkles, 2)
sleep(1)
clear()
typewrite("ready?", 2)
sleep(1)
input("\npress enter")
sleep(1)
clear()
typewrite("\nok, here is your answer ...", 2)
sleep(1)
clear()
typewrite("\nthe magic 8 ball says.....", 3)
clear()
sleep(1)
typewrite(magicsparkles, 2)
typewrite(choice(Ball.outcomes), 5)
for i in range(10):
    typewrite(magicsparkles,0.5)

