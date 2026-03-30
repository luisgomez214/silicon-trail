from game.events import run_events


def apply_passive_effects(state):
    state.hype = max(0, state.hype - 1)

    if state.hype > 80 and state.bugs > 20:
        print("Your product is overhyped and breaking! Morale drops.")
        state.morale -= 10

    if state.bugs > 35:
        print("Your product is unstable! Progress slowed.")
        state.progress = max(0, state.progress - 3)

    if state.hype < 20:
        print("No one is talking about you. Progress slows.")
        state.progress = max(0, state.progress - 2)

    if state.coffee == 0:
        print("Out of coffee. Team is exhausted.")
        state.morale -= 3

    if state.cash > 90000:
        print("Investors notice you're not spending. Hype fades.")
        state.hype = max(0, state.hype - 2)

    if state.morale == 100 and state.progress < 20 and state.day > 5:
        print("Team is comfortable but not shipping. Hype drops.")
        state.hype = max(0, state.hype - 3)

    if state.bugs < 15:
        state.bugs += 1
    else:
        state.bugs += 2


def check_game_over(state):
    if state.progress >= 100:
        print(f"\nCongratulations, {state.company_name}!")
        print("You made it to San Francisco and launched successfully!")
        state.game_over = True
        return True

    if state.cash <= 0:
        print(f"{state.company_name} ran out of cash. Your startup shut down.")
        state.game_over = True
        return True

    if state.morale <= 0:
        print(f"The {state.company_name} team burned out and quit.")
        state.game_over = True
        return True

    if state.bugs >= 60:
        print(f"{state.company_name}'s product is too buggy. Users abandoned it.")
        state.game_over = True
        return True

    if state.hype > 80 and state.bugs > 30:
        print("You overhyped a broken product. Public backlash destroyed your startup.")
        state.game_over = True
        return True

    if state.day > 30:
        print("You ran out of time before launching.")
        state.game_over = True
        return True

    return False


def end_day(state):
    apply_passive_effects(state)
    run_events(state)
    state.bought_coffee_today = False
    check_game_over(state)
