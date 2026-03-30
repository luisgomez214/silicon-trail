from game.actions.base import Action

class Save(Action):
    name = "Save Game"
    description = "Save your progress to disk"

    def can_execute(self, state):
        return True, ""

    def execute(self, state):
        state.wants_save = True  # engine checks this flag
