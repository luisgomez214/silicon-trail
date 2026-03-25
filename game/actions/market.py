from game.actions.base import Action

class Market(Action):
    name = "Marketing"
    description = "Increase hype, costs cash"

    def can_execute(self, state):
        return True, ""

    def execute(self, state):
        print("Marketing...")
        state.hype += 10
        state.cash -= 5000
        state.bugs += 2   # more users → more bugs found
