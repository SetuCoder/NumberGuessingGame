import random
import math

print("‎")
# printing the info
print("- Please give the range of the numbers you wish to guess from.")
print("- Any other characters other than numbers or empty bounds will result in a error in the terminal.")
print("- The program will tell you if your number is too high or too low depending on your guess.")
print("- Your number of chances to guess a number varies by the range you've given.")
print("‎")

lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
print("\n\tYou've only ",
      round(math.log(upper - lower + 1, 2)),
      " chances to guess the number what I'm thinking of!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1

    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try(ies)")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")

if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
