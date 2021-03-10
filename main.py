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
my_choice = [rock, paper, scissors]
computer_choice = [rock, paper, scissors]
my_choice = my_choice[choice]
print(f"You choose {my_choice}")
print(f"Computer chose {computer_choice[2]}")