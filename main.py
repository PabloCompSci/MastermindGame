'''
Pablo Bedolla
Monday January 18, 2021
AP Computer Science
'''
# Imports & Functions
import random
from random import randint
from termcolor import colored
# termcolor import allows for ASCII color change
def gameDesign():
  print(colored('___  ___          _                      _           _ ', 'green')) 
  print(colored('|  \/  |         | |                    (_)         | |', 'green'))
  print(colored('| .  . | __ _ ___| |_ ___ _ __ _ __ ___  _ _ __   __| |', 'green'))
  print(colored("| |\/| |/ _` / __| __/ _ | '__| '_ ` _ \| | '_ \ / _` |", 'green'))
  print(colored('| |  | | (_| \__ | ||  __| |  | | | | | | | | | | (_| |', 'green'))
  print(colored("\_|  |_/\__,_|___/\__\___|_|  |_| |_| |_|_|_| |_|\__,_|\n", 'green'))
gameDesign()
def gameRules():
  print("These are the game rules: ")
  print("1.) There's is a secret message with four hidden numbers, you must guess all four numbers in the correct order to be able to win.")
  print("2.) If you guess all four numbers correct, you win and the game is over.")
  print("3.) If you do not guess all four numbers in the correct order, you will go again until the objective is met.\n")
  print('Example:\n"Please enter your guess ↓"\n Number: 1\n Number: 4\n Number: 5\n Number: 5\n You got 3 numbers correct.\n Try Again" \n')
  print("Now that you've seen an example, it's time to give it a go! Good luck!\nNote: Please use integer inputs only. Using a character will prompt an error message.\n")
gameRules()

# ------------------------------------------------

secretNumber = []
userGuess = []
totalTries = 0
indexRight = 0

def secretNumberGen (secretNumber):
  # Generate Random Secret Number
  for s in range(4):
    secret = random.randint(1,9) # random int from 1 - 9
    secretNumber.append(secret) # add that int to list
secretNumberGen(secretNumber) # Parameter makes secretNumber defined

# User gets to guess
# Whie loop for Guessing
while True:
  print("Please enter your guess ↓ ")
  totalTries += 1

  # User prompted to imput
  try:
    for g in range(4):
      guess = int(input("Number: "))
      userGuess.append(guess)
  # If user enter char, error displayed and continued
  except ValueError:
    print(colored("ERROR: Please enter an Integer", 'red'))
    continue

  # If input int corresponds with index, += 1 indexRight
  if userGuess[0] == secretNumber[0]:
    indexRight += 1
  if userGuess[1] == secretNumber[1]:
    indexRight += 1
  if userGuess[2] == secretNumber[2]:
    indexRight += 1
  if userGuess[3] == secretNumber[3]:
    indexRight += 1
  # Total number of integers correct returned
  print("You got " + str(indexRight) + " numbers correct.")

  # If user guesses all correct message returned
  if secretNumber == userGuess:
    if totalTries > 1:
      print(colored("Congratulations, you win! It took you a total of " + str(totalTries) + " tries.", 'yello'))
    else:
      print(colored("Congratulations, you win! It took you a total of " + str(totalTries) + " try.", 'yellow'))
    False
    break

  # If user does not guess all correct message returned
  elif secretNumber != userGuess:
    indexRight = 0    # correct numbers reseted
    del userGuess[:]  # input list reseted
    print("Try again")
  else:
    pass

