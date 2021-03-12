import random
import os

while True:
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

    choice = int(input("What do you choose? Type 0 for Rock, 1 paper or 2 for Scisor. "))
    possible_choices = [rock, paper, scissors]
    user_choice = possible_choices[choice]
    random_index = random.randint(0,len(possible_choices)-1)
    c_choice = possible_choices[random_index]

    print(f"\nYou choose {user_choice} \ncomputer chose {c_choice}.\n")

    if user_choice == c_choice:
      print("It's a tie!")
    elif user_choice == rock:
      if c_choice == scissors:
        print("Rock smashes scissors! You win!")
      else:
        print("Paper covers rock! You lose.")
    elif user_choice == paper:
      if c_choice == rock:
        print("Paper covers Rock! You win!")
      else:
        print("Scissors cuts papers! You loose.")
    elif user_choice == scissors:
      if c_choice == paper:
        print("Scissors cut paper! You win!")
      else:
        print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (Enter/y/n):")
    clear = lambda: os.system('clear')
    clear()
    if play_again.lower() == "n":
        break