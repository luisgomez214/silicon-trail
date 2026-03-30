from game.actions.base import Action

class Rest(Action):
    name = "Rest"
    description = "Recover morale using coffee"

    def can_execute(self, state):
        if state.coffee < 5:
            return False, "Not enough coffee to rest properly."
        if state.morale >= 90:
            return False, "Your team is already well-rested."
        return True, ""

    def execute(self, state):
        state.morale += 20  # was 15
        state.coffee -= 5   # was 10
        state.morale = min(100, state.morale)
        state.coffee = max(0, state.coffee)
        print("Resting...")
