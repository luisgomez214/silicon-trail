from game.actions.base import Action

class BuyCoffee(Action):
    name = "Buy Coffee"
    description = "Spend cash to restock coffee ($3,000)"

    def can_execute(self, state):
        if state.cash < 3000:
            return False, "Not enough cash to buy coffee."
        if state.coffee >= 80:
            return False, "Coffee supply is already high."
        if getattr(state, 'bought_coffee_today', False):
            return False, "Already restocked coffee today."
        return True, ""

    def execute(self, state):
        state.cash -= 3000
        state.coffee = min(80, state.coffee + 20)
        state.bought_coffee_today = True
        state.free_action = True
        print("Restocked coffee supply.")
