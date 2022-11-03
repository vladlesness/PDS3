from random import randint
import sys


def guess_num():
    rand_n = randint(0, 100)
    tries = 6
    start = 0
    end = 100
    while tries > 0:
        try_word = 'tries'
        if tries == 1:
            try_word = 'try'
        mid = (start + end) // 2
        try:
            guess = int(input(f'You have {tries} {try_word}.\nGuess the number from {start} to {end}: '))
        except Exception as ex:
            print(ex, file=sys.stderr)
            continue
        if rand_n == guess:
            print(f'You win and guessed on try {7-tries}!')
            break
        elif guess < rand_n and tries != 1:
            print('Your number is smaller.\nTry again!\n')
            start = mid + 1
        elif guess > rand_n and tries != 1:
            print('Your number is bigger.\nTry again!\n')
            end = mid - 1
        else:
            print('You lost!')
        tries -= 1
