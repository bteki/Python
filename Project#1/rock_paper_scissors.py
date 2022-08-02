"""

import random

def play():
    user = input("'r' for Rock, 'p' for Paper, & 's' for Scissors: \n")
    computer = random.choice(['r', 'p', 's'])

    #game rules
    # if user = computer play again
    # if user = r & computer = s, user gets a point
    # if user = s & computer = p, user gets a point
    # if user = p & computer = r, user gets a point
    # if user = r & computer = p, computer gets a point
    # if user = p & computer = s, computer gets a point
    # if user = s & computer = r, computer gets a point

    if user == computer:
        return 'tie'


    if is_win(user, computer):
        return 'You Won!!!'

    return 'You Lost'

 def is_win(player, opponent):
    if ( player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
"""
import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())




