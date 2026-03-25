from game.actions.base import Action
import random

class Travel(Action):
    name = "Travel"
    description = "Move forward, costs morale and coffee"

    def can_execute(self, state):
        if state.coffee < 5:
            return False, "Not enough coffee."
        if state.morale < 5:
            return False, "Team morale too low."
        if state.progress >= 100:
            return False, "You’ve already arrived."
        return True, ""

    def execute(self, state):
        outcome = random.choice(["good", "normal", "bad", "terrible"])

        if outcome == "good":
            print("Smooth travel! Great progress.")
            state.progress += 15
            state.cash -= 1500

        elif outcome == "normal":
            print("Travel was steady.")
            state.progress += 10
            state.cash -= 2000
        
        elif outcome == "terrible":
            print("Travel was terrible.")
            state.progress += 0
            state.cash -= 5000
            state.bugs += 10

        else:
            print("Travel issues slowed you down.")
            state.progress += 5
            state.cash -= 3000
            state.bugs += 5

        state.coffee -= 5
        state.morale -= 5
