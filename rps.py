#makena kong
#Girls Who Code - technical project
#rock paper scissors game

import sys
import random
from random import randrange

def main():

   print("\t\t\tWelcome to the game.")
   print("You will be playing Rock, Paper, Scissors against me, the computer.")
   print("\t\t\t\tGoodLuck!\n")

   is_done = True
   while (is_done):
      user_input = input("Your choice: ")
      comp_input = random_choice()
      print("My choice:", comp_input)

      res = get_results(user_input, comp_input)
      if (res == -1):
         print(user_input + " beats " + comp_input)
         print("\nYou win!\n")
         is_done = False
      elif (res == 1):
         print(comp_input + " beats " + user_input)
         print("\nI win!\n")
         is_done = False
      elif (res == 0):
         print("\nIts a tie - try again\n")
      else:
         print("Your input was invalid - try again\n")

      if (not is_done):
         choice = input("Would you like to play again? Y/N: ")
         if (choice.lower() == 'y'):
            is_done = True
            print()
         elif (choice.lower() == 'n'):
            is_done = False
            print("Thanks for playing!")

#generates random choice
def random_choice():
   options = ["rock","paper","scissors"]
   rand_num = randrange(0,3)
   return options[rand_num]

#returns -1 for user, 1 for computer, 0 for tie
def get_results(choice1, choice2):
   choice1 = choice1.lower()
   if (choice1.lower() == choice2):
      return 0
   elif (choice1 == "rock"):
      if (choice2 == "scissors"):
         return -1
      else:
         return 1
   elif(choice1 == "paper"):
      if (choice2 == "rock"):
         return -1
      else:
         return 1
   elif(choice1 == "scissors"):
      if (choice2 == "paper"):
         return -1
      else:
         return 1
   else:
      return 2
   return 2

if __name__ == "__main__":
   main()
