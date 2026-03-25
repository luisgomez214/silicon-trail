from game.actions.base import Action

class Work(Action):
    name = "Work"
    description = "Reduce bugs, costs morale"

    def can_execute(self, state):
        return True, ""

    def execute(self, state):
        print("Working...")
        state.bugs -= 10
        state.morale -= 5
        state.hype += 3

        state.bugs = max(0, state.bugs)
