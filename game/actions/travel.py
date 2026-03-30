from game.actions.base import Action
from api.weather import LOCATIONS
import random

class Travel(Action):
    name = "Travel"
    description = "Move forward, costs money, morale, and coffee"

    def can_execute(self, state):
        if state.coffee < 5:
            return False, "Not enough coffee."
        if state.morale < 5:
            return False, "Team morale too low."
        if state.progress >= 100:
            return False, "You've already arrived."
        return True, ""


    def execute(self, state):
        # weather influences outcome probabilities
        if state.weather in ["rain", "storm", "fog"]:
            outcomes = ["good", "normal", "bad", "terrible", "terrible", "bad"]
            print("Bad weather makes travel harder.")
        elif state.weather == "sunny":
            outcomes = ["good", "good", "normal", "normal", "bad", "terrible"]
            print("Clear skies help the journey.")
        else:
            outcomes = ["good", "normal", "bad", "terrible"]

        outcome = random.choice(outcomes)

        if outcome == "good":
            print("Smooth travel! Great progress.")
            state.progress += 20
            state.cash -= 1500

        elif outcome == "normal":
            print("Travel was steady.")
            state.progress += 15
            state.cash -= 2000

        elif outcome == "terrible":
            print("Travel was terrible.")
            state.progress += 2
            state.cash -= 5000
            state.bugs += 6

        else:
            print("Travel issues slowed you down.")
            state.progress += 8
            state.cash -= 3000
            state.bugs += 3

        state.coffee -= 5
        state.morale -= 5

        new_index = min(state.progress // 10, len(LOCATIONS) - 1)
        if new_index > state.location_index:
            city = LOCATIONS[new_index][0]
            print(f"You've reached {city}.")
        state.location_index = new_index
