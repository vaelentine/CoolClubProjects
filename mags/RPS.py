# Rock paper scissors game
import random
from os import system, name
from time import sleep

# TODO: rpsls



# -1, lose; 0, tie; 1, win
class Player:
    wins = 0
    losses = 0
    ties = 0
    game_chosen = "RPS"
    hand_choice = None

    def assign_wins(self, score_int):
        if score_int == -1:
            print("Player loses!")
            self.losses += 1
        elif score_int == 1:
            print("Player wins!")
            self.wins += 1
        else:
            self.ties += 1

    def get_score(self):
        print(f"Player score:\nWins: {self.wins}\nLosses: {self.losses}\nTies: {self.ties}")

# For storing all of the game logic and methods
class RPS:
    name = "Rock, Paper, Scissors"
    choices = ["rock", "paper", "scissors"]
    win = [0, -1, 1], [1, 0, -1], [-1, 1, 0]
    outcomes = ["rock smashes scissors!", "paper covers rock!", "scissors cut paper!", "Tie!"]

    def __init__(self, player_choice, computer_choice):
        # get attack statement
        comparison = [self.choices.index(player_choice), self.choices.index(computer_choice)]
        # print(f"comparison: {comparison}")
        if 0 in comparison and 2 in comparison:
            self.attack_round = self.outcomes[0]
            # print("outcome 0!")
        elif 0 in comparison and 1 in comparison:
            self.attack_round = self.outcomes[1]
            # print("outcome 1!")
        elif 1 in comparison and 2 in comparison:
            self.attack_round = self.outcomes[2]
            # print("outcome 2")
        else:
            self.attack_round = self.outcomes[3]

        # assign winner
        self.current_winner = self.win[comparison[0]][comparison[1]]

# class Game:
# Extra functions
# to clear the console of all of that messy text
def clear():
    #windows
    if name == 'nt':
        _ = system('cls')
    # for unix based
    else:
        _ = system('clear')

    print(end='\n\n\n')
# for making thinking dots so you know stuff is happening
def dot_printer(time):
    print('.', end=" ")
    sleep(time)
    print('.', end=" ")
    sleep(time)

def comp_choose(choices):
    return random.choice(choices)

def play_game(game_chosen):
    player = Player()
    game = True
    while game == True:
        clear()
        print(f"Whee! Let's play {game_chosen.name}!!")
        sleep(1)

        # computer choose
        print('\nFirst, the computer is choosing an attack')
        comp_choice = comp_choose(game_chosen.choices)
        dot_printer(1)
        print("\nThe computer has chosen!")
        sleep(2)
        clear()

        # player choose
        print('Now the player will choose.')
        print('\nChoose from the following:')
        for choice in game_chosen.choices:
            print(f"{game_chosen.choices.index(choice) + 1}. {choice}")
        player_choice = False
        while not player_choice:
            choice_attempt = input("\nYour choice?  ")
            try:
                player_choice = game_chosen.choices[int(choice_attempt) -1]
            except:
                clear()
                print(f"I'm sorry. {choice_attempt} is not a valid choice.")
                print('Choose from the following:')
                for choice in game_chosen.choices:
                    print(f"{game_chosen.choices.index(choice) + 1}. {choice}")
        clear()
        print(f"Awesome! Player chooses {player_choice}.")
        sleep(1)
        clear()
        # compare
        print("Ok. Now let's play!")
        sleep(1)
        clear()
        print("\nWe'll go on three.")
        print("\n1")
        sleep(1)
        print("2")
        sleep(1)
        print("GO!")
        sleep(0.5)
        clear()
        print(f"computer chooses {comp_choice}!")
        sleep(1)
        print(f"Player chooses {player_choice}!")
        sleep(1)
        rps = RPS(player_choice, comp_choice)
        player.assign_wins(rps.current_winner)
        print(rps.attack_round)
        sleep(2)
        clear()
        player.get_score()
        sleep(2)
        while True:
            again = input("\nPlay again? (Y/N)")
            if again.upper() == "Y":
                break
            elif again.upper() == "N":
                game = False
                print("Be seeing you!")
                break
        # record score
        # ask player to play again

play_game(RPS)
