import random

options = ['rock', 'paper', 'scissors']

user = input('rock, paper, or scissors? ')


if user not in options:
    print('\033[1m\033[31mInvalid input!\033[0m')
else:
    python = random.choice(options)
    print(f'\033[1mYou choose \033[32m{user}\033[0m \n\033[1mPython choose \033[32m{python}\033[0m')

    if user == python:
        print('\033[3m\033[35mIt\'s a tie!\033[0m')
    elif user == 'rock' and python == 'scissors' or user == 'paper' and python == 'rock' or user == 'scissors' and python == 'paper':
        print('\033[3m\033[35mYou win!\033[0m')
    else:
        print('\033[3m\033[35mYou lose!\033[0m')