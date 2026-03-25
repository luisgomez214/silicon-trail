from game.actions.base import Action

class BuyCoffee(Action):
    name = "Buy Coffee"
    description = "Spend cash to restock coffee"

    def can_execute(self, state):
        if state.cash < 2000:
            return False, "Not enough cash to buy coffee."
        if state.coffee >= 100:
            return False, "Coffee already full."
        return True, ""

    def execute(self, state):
        state.cash -= 2000
        state.coffee = min(100, state.coffee + 20)
