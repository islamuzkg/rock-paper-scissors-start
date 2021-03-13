import random
import os

#while True:
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 paper or 2 for Scisor. "))
possible_choices = [rock, paper, scissors]

if user_choice >= 3 or user_choice < 0:
  print("You entered out of range number, please try again.")
else:
  print(possible_choices[user_choice])

c_choice = random.randint(0, 2)
print("Cmputer chose:\n")
print(possible_choices[c_choice])
#[rock, paper, scissors]
#options = [[draw, lose, win], [win, draw, lose], [lose, win, draw]
if user_choice == c_choice:
  print("It is a Draw!")
elif user_choice == 0 and c_choice == 2:
  print("You win!")
elif c_choice == 0 and user_choice == 2:
  print("You lose!")
elif c_choice > user_choice:
  print("You lose")
elif user_choice > c_choice:
  print("You win!")




    # play_again = input("Play again? (Enter/y/n):")
    # clear = lambda: os.system('clear')
    # clear()
    # if play_again.lower() == "n":
    #     break