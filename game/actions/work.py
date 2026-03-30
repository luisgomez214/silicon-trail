from game.actions.base import Action
import random

class Work(Action):
    name = "Work"
    description = "Reduce bugs, earn cash, costs morale"

    def can_execute(self, state):
        if state.morale < 5:
            return False, "Team is too burned out to work."
        return True, ""

    def execute(self, state):
        print("Working...")
        state.bugs -= 12
        state.morale -= 10
        state.hype += 3
        state.bugs = max(0, state.bugs)

        if state.morale >= 70:
            earned = random.randint(3000, 5000)
        elif state.morale >= 40:
            earned = random.randint(1500, 3000)
        else:
            earned = random.randint(500, 1500)
            print("Low morale is hurting productivity.")

        state.cash += earned
        print(f"Shipped some features. Earned ${earned:,}.")
