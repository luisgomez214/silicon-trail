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
        return state.bugs > 25 and random.random() < 0.2

    def execute(self, state):
        state.bugs += 5
        state.morale -= 3
        state.bugs = max(0, state.bugs)
        print("A critical bug appeared!")


class WeatherEvent(Event):
    name = "Weather"

    def can_trigger(self, state):
        return True

    def execute(self, state):
        if state.weather == "sunny":
            state.morale = min(100, state.morale + 3)
            print("Beautiful day. Team morale is up.")

        elif state.weather == "rain":
            state.progress = max(0, state.progress - 2)
            print("Rain slowed everything down.")

        elif state.weather == "cold":
            state.coffee = max(0, state.coffee - 2)
            print("Cold weather — team is burning through coffee.")

        elif state.weather == "heat":
            state.morale = max(0, state.morale - 3)
            state.coffee = max(0, state.coffee - 1)
            print("Brutal heat. Team is drained.")

        elif state.weather == "cloudy":
            pass  

        elif state.weather == "storm":
            state.bugs += 3
            state.morale = max(0, state.morale - 5)
            print("Thunderstorm hits. Servers are down, bugs everywhere.")

        elif state.weather == "fog":
            state.progress = max(0, state.progress - 1)
            print("Foggy day. Everything moves slower.")

EVENTS = [
    CriticalBug(),
    WeatherEvent(),
]


def run_events(state):
    for event in EVENTS:
        if event.can_trigger(state):
            event.execute(state)
