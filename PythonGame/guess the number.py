# the computer guessed number 1-50 and 6 attempts
import random

tries = 0
number = random.randint(1, 50)
print('Hmm Try to guess what number between 1 and 50 was thinking about:')

while tries < 6:
    guess = int(input('Taken a guess:'))

    tries += 1

    if guess < number:
        print('Your guess is too low')

    if guess > number:
        print('Your guess is too high')
    if guess == number:
        print(f'Congratulations! You guessed my number in {tries} guesses')
    if guess != number and tries == 6:
        print(f"Sorry, but you didn't make it. My number was: {number}")