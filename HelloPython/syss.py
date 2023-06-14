from random import randint
import sys

# Generate a number within the specified range
answer = randint(1,10)

while True:
    try:
        print(answer)
        guess = int(input('Guess a number from 1 to 10: '))
        if 1 <= guess <= 10:
            if guess == answer:
                print('You guessed it right!')
                break
            else:
                print('Wrong guess. Try again!')
        else:
            print('Please enter a number between 1 and 10.')
    except ValueError:
        print('Please enter a valid number.')
