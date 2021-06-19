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

map = [rock, paper, scissors]

result_map = [["Draw", "You lose", "You win"], ["You win", "Draw", "You lose"], ["You lose", "You win", "Draw"]]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissros: "))

print(f"You chose: {map[user_choice]}")

computer_choice = random.randint(0, 2)

print(f"Computer chose: {map[computer_choice]}")

print(result_map[user_choice])