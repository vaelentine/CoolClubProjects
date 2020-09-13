# create and store a random number between 1 and 100
import random
number = random.randint(1, 100)

# print "I have a number between 1 and 100, guess that shit"
print("I am thinking of a number between 1 and 100. Can you guess the number?")
guess = int(input())

# running tally of how many guesses
guess_count = 1

# compare guess to number
while guess != number:
    # if number is too high, print that it is too high
    if guess > number:
        print("My number is lower than that. Guess again.")
    # if number is too low, print that it is too low
    elif guess < number:
        print("My number is higher than that. Guess again.")
    print("you have guessed " + str(guess_count) + " times.")
    guess = int(input())
    guess_count += 1


# if number is correct, print "you be the winner yeehaw"
print("THAT IS MY NUMBER! YOU ARE THE BEST GUESSER EVER!")
print("It took you " + str(guess_count) + " guesses!")



