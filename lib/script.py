import random
from capitals import states

# print(states)

def play_game():
    print('Heyy, This is the State Capital Guessing Game!/n')
    score = 0

states_copy = states[:]

while states_copy:
    state_obj = random.choice(states_copy)
    state = state_obj['name']
    capital = state_obj['capital']
    states_copy.remove(state_obj)

    guess = input(f'What is the Capital of {state}? ').strip().title()

if guess == capital:
      print('Correct!')
      score =+ 1 
else: 
      print(f'Incorrect. The Capital of {state} is {capital}.')

print(f"/nYou scored {score} out of {len(states)}.")


play_again = input('Do you want to play again? (yes/no) ').strip().lower()
if play_again == 'yes':
    play_game()
else:
    print('Thanks for playing!')


play_game()
      
