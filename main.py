import random
import math

print("‎")
# printing the info
print("- Please give the range of the numbers you wish to guess from.")
print("- Any other characters other than numbers or empty bounds will result in a error in the terminal.")
print("- The program will tell you if your number is too high or too low depending on your guess.")
print("- Your number of chances to guess a number varies by the range you've given.")
# I don't know how to do a line break between print and inputs
print("‎")

# Taking Inputs
lower = int(input("Enter Lower bound:- "))

# Taking Inputs
upper = int(input("Enter Upper bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the number what I'm thinking of!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if x == guess:
        print("Congratulations you did it in ",
              count, " try(ies)")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

# Better to use This source Code on pycharm!