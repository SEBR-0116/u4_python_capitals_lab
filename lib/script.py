# from capitals import states

# print(states)

# import random
# from capitals import states

# def play_quiz():
#     correct_answers = 0
#     incorrect_answers = 0
    
#     # Shuffle the list of states
#     random.shuffle(states)
    
#     for state in states:
#         state_name = state["name"]
#         correct_capital = state["capital"]
        
#         # Prompt user for input
#         user_input = input(f"What is the capital of {state_name}? ").strip().title()
        
#         # Check if the input is correct
#         if user_input == correct_capital:
#             print("Correct!")
#             correct_answers += 1
#         else:
#             print(f"Sorry, the correct answer is {correct_capital}.")
#             incorrect_answers += 1
    
#     # Print final score
#     print(f"Quiz ended. You got {correct_answers} correct answers and {incorrect_answers} incorrect answers.")

# # Main loop
# while True:
#     play_quiz()
#     play_again = input("Do you want to play again? (yes/no): ").strip().lower()
#     if play_again != "yes":
#         print("Thank you for playing. Goodbye!")
#         break

import random

from capitals import states

def play_quiz():
    correct_answers = 0
    incorrect_answers = 0

    #Shuffle the states
    random.shuffle(states)

    for state in states:
        state_name = state["name"]
        correct_capital = state["capital"]

        #Prompt user for answer
        user_input = input(f"What is the capital of {state_name}? ").strip().title()

        #Check if the input is correct
        if user_input == correct_capital:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is {correct_capital}.")
            incorrect_answers += 1 

    #Print final score
    print(f"Quiz completed. You got {correct_answers} capitals correct and {incorrect_answers} capitals incorrect.")


#Game Loop
while True:
    play_quiz()
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thank you for playing. Goodbye!")
        break