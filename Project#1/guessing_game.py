import random
'''
def guess(x):
    rand_num = random.randint(1, x)
    guess = 0
    while guess != rand_num:
        guess = int (input(f'Guess a number between 1 and {x}: '))
        if guess < rand_num:
            print("Sorry too low, guess again: ")
        elif guess > rand_num:
            print("Sorry too high, guess again: ")
    print (f'YAY, you did! you guessed the number {rand_num} correctly!!!')
'''

# the computer is going to guess the random num given by the user
def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ')
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1

    print(f'YAY!!! the computer guessed your number {guess}, correctly!!!')

comp_guess(100)






