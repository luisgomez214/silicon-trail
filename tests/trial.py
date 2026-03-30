import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game.state import GameState
from game.actions import ACTIONS
from api.weather import get_weather
from game.rules import end_day


def run_trial(name, company_name, inputs):
    print(f"\n{'=' * 50}")
    print(f"TRIAL: {name}")
    print(f"Company: {company_name}")
    print("=" * 50)

    state = GameState()
    state.company_name = company_name
    input_queue = list(inputs)

    while not state.game_over and input_queue:
        condition, temp, city = get_weather(state.location_index)
        state.weather = condition

        choice_index = input_queue.pop(0) - 1

        if choice_index < 0 or choice_index >= len(ACTIONS):
            print(f"Day {state.day}: invalid choice")
            continue

        action = ACTIONS[choice_index]
        can_do, reason = action.can_execute(state)

        if not can_do:
            print(f"Day {state.day}: BLOCKED: {action.name} — {reason}")
        else:
            action.execute(state)

        if getattr(state, "wants_save", False):
            print(f"Day {state.day}: save requested")
            state.wants_save = False
            break

        if getattr(state, "free_action", False):
            state.free_action = False
            continue

        end_day(state)

        print(
            f"Day {state.day}: {action.name} | "
            f"Cash ${state.cash} | Morale {state.morale} | Coffee {state.coffee} | "
            f"Bugs {state.bugs} | Hype {state.hype} | Progress {state.progress}% | Weather {condition}"
        )

        if not state.game_over:
            state.day += 1

    if not state.game_over:
        print(f"\nRESULT: inputs exhausted on day {state.day}")
        print(
            f"Final: Cash ${state.cash} | Morale {state.morale} | "
            f"Bugs {state.bugs} | Progress {state.progress}%"
        )


if __name__ == "__main__":
    run_trial(
        "Balanced Strategy",
        "Luis LLC",
        [3, 1, 1, 2, 3, 1, 1, 2, 3, 1, 1, 2],
    )

    run_trial(
        "Travel Rush",
        "Luis LLC",
        [1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 1, 2],
    )

    run_trial(
        "Marketing Strategy",
        "Luis LLC",
        [4, 4, 3, 1, 4, 3, 1, 2, 4, 3, 1, 1],
    )
