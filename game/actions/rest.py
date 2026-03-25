from game.actions.base import Action

class Rest(Action):
    name = "Rest"
    description = "Recover morale using coffee"

    def can_execute(self, state):
        return True, ""

    def execute(self, state):
        state.morale += 10
        state.coffee -= 5
        state.morale = min(100, state.morale)
        state.coffee = max(0, state.coffee)
        print("Resting...")
