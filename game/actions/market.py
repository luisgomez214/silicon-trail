from game.actions.base import Action

class Market(Action):
    name = "Marketing"
    description = "Boost hype, attract users, earn revenue"

    def can_execute(self, state):
        if state.cash < 1000:
            return False, "Not enough cash to run a campaign."
        return True, ""

    def execute(self, state):
        print("Marketing...")
        state.hype += 15
        state.cash -= 1000   # was 2000
        state.bugs += 1

        if state.hype >= 60:
            revenue = 8000
            print("Campaign went viral! Revenue spike: $8,000.")
        elif state.hype >= 40:
            revenue = 4000
            print("Campaign performed well. Revenue: $4,000.")
        else:
            revenue = 2000
            print("Campaign had limited reach. Revenue: $2,000.")

        state.cash += revenue
