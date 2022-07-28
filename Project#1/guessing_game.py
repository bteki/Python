import random

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

guess(10)






