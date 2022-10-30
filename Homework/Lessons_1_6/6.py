from random import randint


#                                       PSEUDO CODE
# Create a function and name it guess_num.
# Create a variable that will generate a random integer 0 to 100.
# Create a tries variable that will be the condition for a while loop. The variable will be an int number of tries.
# Create start and end variables to show the user in which range of numbers they should look
# and update them on each loop.
# A While loop will iterate 6 times at most until tries is 0 or the user guesses the random number.
#   With each loop show the user the guess range and update it(start and end) with binary search.
#   Create a variable that will represent the middle of our range and update it on each loop with (start+end) // 2.
#   If the random equals the user's number
#       print that the user guessed and break the loop
#   Else if the user's number is smaller than the random and tries does not equal 1
#       print that the user's number is smaller and update start with middle + 1.
#   Else if the user's number is bigger than the random and tries does not equal 1
#       print that the user's number is bigger and update end with middle - 1.
#   Else print that the user lost.
#   At the end of each loop tries will decrease by 1 so the user has 6 times to guess.
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
        guess = int(input(f'You have {tries} {try_word}.\nGuess the number from {start} to {end}: '))
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


# Написати програму з використанням рекурсії. Програма повинна приймати з консолі ціле натуральне число.
# Далі, використовуючи функцію, в якій реалізований механізм рекурсії, програма віднімає від заданого числа одиницю і
# виводить у консолі поточне число. Програма повинна припинити роботу, коли число дорівнюватиме нулю.
def negative_count(n):
    if n > 0 and isinstance(n, int):
        print(n)
        n -= 1
    elif n < 0 or not isinstance(n, int):
        print('Your number is below 0 or is not an integer')
        return None
    else:
        return None
    return negative_count(n)
