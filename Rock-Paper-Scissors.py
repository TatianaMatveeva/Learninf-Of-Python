# Write a rock-paper-scissors game against the computer.
# Run the game in an endless loop.
# Request user input (R for rock, S for scissors, P for paper).
# Generate a random selection of a computer.
# Display computer selection.
# Determine the winner by displaying the relevant information.
# Ask the user if he wants to repeat the game.
# If he wants to repeat,he does not want to leave the cycle.

import random

should_continue = True

while should_continue:
    player_choice = input('Player choice: [R/S/P]').lower()

    if player_choice not in ['r','s','p']:
        print('Incorrect. Try again')
        continue
    gen ={1:'r', 2:'s', 3:'p'}
    comp_choice = gen[random.randint(1, 3)]
    print(f'Comp choice = {comp_choice}')

    winning_combinations = [('p', 'r'), ('r', 's'), ('s', 'p')]
    if player_choice == comp_choice:
        print('A draw')
    elif(player_choice, comp_choice) in winning_combinations:
        print('*** Human wins ****'*6)
    else:
        print('*** Comp wins ****'*6)

    should_continue = input("Want to proceed? [y/b]").lower() == 'y'