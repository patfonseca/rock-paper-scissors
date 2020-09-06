import random


def winner(a, b):
    winning_cases = {'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
                     'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
                     'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
                     'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
                     'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
                     'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
                     'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
                     'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
                     'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
                     'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
                     'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
                     'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
                     'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
                     'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
                     'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']}
    if a in winning_cases:
        if b in winning_cases[a]:
            return a
        else:
            return b


user_option = ''
player_name = input('Enter your name:')
player_score = 0

file = open('rating.txt', 'r')
for line in file:
    rating_list = line.split()
    if rating_list[0] == player_name:
        player_score = int(rating_list[1])
        break
file.close()

choices = ['']

print('Hello,', player_name)
choices = input().split(',')
if choices == ['']:
    choices = ['rock', 'scissors', 'paper']
print("Okay, let's start")

while True:

    user_option = input()

    if user_option in choices:
        computer_option = choices[random.randint(0, len(choices) - 1)]
        if user_option == computer_option:
            print('There is a draw (' + user_option + ')')
            player_score += 50
        elif user_option == winner(user_option, computer_option):
            print('Well done. The computer chose', computer_option, 'and failed')
            player_score += 100
        else:
            print('Sorry, but the computer chose', computer_option)

    elif user_option == '!rating':
        print('Your rating:', player_score)
    elif user_option == '!exit':
        break
    else:
        print('Invalid input')

print('Bye!')