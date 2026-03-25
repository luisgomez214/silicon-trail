class Action:
    name = ""
    description = ""

    def can_execute(self, state):
        return True, ""

    def execute(self, state):
        raise NotImplementedError
