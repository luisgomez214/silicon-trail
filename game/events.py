import random


class Event:
    name = ""

    def can_trigger(self, state):
        return True

    def execute(self, state):
        pass


class CriticalBug(Event):
    name = "Critical Bug"

    def can_trigger(self, state):
        return state.bugs > 20

    def execute(self, state):
        state.bugs += 10
        state.morale -= 5
        state.bugs = max(0, state.bugs)
        print("A critical bug appeared!")


class Rain(Event):
    name = "Rain"

    def can_trigger(self, state):
        return state.weather == "rain"

    def execute(self, state):
        state.progress -= 3
        state.progress = max(0, state.progress)
        print("Rain slowed everything down.")


class Cold(Event):
    name = "Cold"

    def can_trigger(self, state):
        return state.weather == "cold"

    def execute(self, state):
        state.coffee -= 2
        print("Cold weather increases coffee consumption.")


EVENTS = [
    CriticalBug(),
    Rain(),
    Cold(),
]


def run_events(state):
    possible_events = [e for e in EVENTS if e.can_trigger(state)]

    if possible_events:
        event = random.choice(possible_events)
        event.execute(state)
