import random

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
game = [rock, paper, scissors]

user_choice = int(input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors "))
if user_choice >=3 or user_choice < 0:
    print("your input is wrong, you lose.")
else:
    print(game[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer choice: ")
    print(game[computer_choice])   

if user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw")
