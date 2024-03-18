from capitals import states
import random

states_list = [*states]
random.shuffle(states_list)

class Game:
    def __init__(self):
        self.game_running = False
        self.player_score = 0
        self.current_round = 0
        print("Game Loading... Please Wait")

    def game_over(self):
        self.game_running = False
        print(f"Your Score was: {self.player_score}")

    def game_start(self):
        self.game_running = True
        while self.game_running and (self.current_round < len(states_list)):
            print(f"The state is: {states_list[self.current_round]['name']}")
            user_guess = input("Please input your guess: ")
            if user_guess == states_list[self.current_round]["capital"]:
                self.player_score += 1
                print("Nice Job! Keep Going")
                print(f"Current Score: {self.player_score}")
                self.current_round += 1 
            else:
                print(f"The correct guess was: {states_list[self.current_round]["capital"]}")
                self.game_over()

    def welcome_message(self):
        print("Welcome to StateGuesser - US Edition")
        print("""Wanna play?
              1 - Yes
              2 - No""")
        user_choice = input("Please make a selection (For example: 1): ")
        if user_choice == "1":
            self.game_start()
        else:
            print("Alright, bye!")

new_game = Game()
new_game.welcome_message()