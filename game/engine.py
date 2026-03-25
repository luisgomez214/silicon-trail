from game.state import GameState
from game.actions import ACTIONS
from api.weather import get_weather
from game.events import run_events

class GameEngine:
    
    def __init__(self):
        self.state = GameState()

    def show_actions(self):
        for i, action in enumerate(ACTIONS, 1):
            print(f"{i}. {action.name} - {action.description}")

    def display_status(self):
        s = self.state
        print(f"\nDay {s.day}")
        print(f"Cash: {s.cash}, Morale: {s.morale}, Coffee: {s.coffee}")
        print(f"Bugs: {s.bugs}, Hype: {s.hype}, Progress: {s.progress}%")

    def apply_choice(self):
        valid_turn = False

        while not valid_turn:
            choice = input("Choice: ")

            try:
                index = int(choice) - 1

                if index < 0 or index >= len(ACTIONS):
                    print(f"Please enter a number between 1 and {len(ACTIONS)}.")
                    continue

                action = ACTIONS[index]
                can_do, reason = action.can_execute(self.state)

                if can_do:
                    action.execute(self.state)
                    valid_turn = True
                else:
                    print(reason)

            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_game_over(self):
        s = self.state

        if s.progress >= 100:
            print("You made it to San Francisco and launched successfully!")
            s.game_over = True
            return

        if s.cash <= 0:
            print("You ran out of cash. Your startup shut down.")
            s.game_over = True
            return

        if s.morale <= 0:
            print("Your team burned out and quit.")
            s.game_over = True
            return

        if s.bugs >= 50:
            print("Your product is too buggy. Users abandoned it.")
            s.game_over = True
            return

        if s.hype > 80 and s.bugs > 30:
            print("You overhyped a broken product. Public backlash destroyed your startup.")
            s.game_over = True
            return

        if s.day > 30:
            print("You ran out of time before launching.")
            s.game_over = True


    def run(self):
        while not self.state.game_over:
            self.display_status()
            self.show_actions()
            self.state.hype = max(0, self.state.hype - 2)

            self.apply_choice()

            if self.state.hype > 80 and self.state.bugs > 20:
                print("Your product is overhyped and breaking! Morale drops.")
                self.state.morale -= 10

            if self.state.bugs > 30:
                print("Your product is unstable! Progress slowed.")
                self.state.progress -= 5

            self.state.weather = get_weather()
            print(f"Weather today: {self.state.weather}")
            self.state.bugs += 2
            run_events(self.state)

            self.check_game_over()
            self.state.day += 1
