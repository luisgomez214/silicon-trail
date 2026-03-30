from game.state import GameState
from game.actions import ACTIONS
from api.weather import get_weather
from game.rules import end_day
import json
import os


class GameEngine:
    def __init__(self):
        self.state = GameState()
        os.makedirs("data", exist_ok=True)

    def show_actions(self):
        for i, action in enumerate(ACTIONS, 1):
            print(f"{i}. {action.name} - {action.description}")

    def display_status(self):
        from api.weather import LOCATIONS
        s = self.state
        city = LOCATIONS[min(s.location_index, len(LOCATIONS) - 1)][0]
        print(f"\n--- Day {s.day} | {city} ---")
        print(f"Cash: ${s.cash:,} | Morale: {s.morale} | Coffee: {s.coffee}")
        print(f"Bugs: {s.bugs} | Hype: {s.hype} | Progress: {s.progress}%")

    def apply_choice(self):
        valid_turn = False
        while not valid_turn:
            choice = input("Choice: ")
            try:
                index = int(choice) - 1
                if index < 0 or index >= len(ACTIONS):
                    print(f"Please enter a number between 1 and {len(ACTIONS)}.")
                    continue
                action = ACTIONS[index]
                can_do, reason = action.can_execute(self.state)
                if can_do:
                    action.execute(self.state)
                    valid_turn = True
                else:
                    print(reason)
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_save_files(self):
        saves = []
        for f in os.listdir("data"):
            if f.startswith("save_") and f.endswith(".json"):
                saves.append(os.path.join("data", f))
        return sorted(saves)

    def show_intro(self):
        print("=" * 50)
        print("           SILICON TRAIL")
        print("=" * 50)

        saves = self.get_save_files()

        if saves:
            print("\n1. New Game")
            print("2. Continue")
            choice = input("\nEnter choice: ").strip()

            if choice == "2":
                print("\nSelect a save:")
                for i, f in enumerate(saves, 1):
                    with open(f) as file:
                        data = json.load(file)
                    company = data.get("company_name", "Unknown")
                    day = data.get("day", "?")
                    progress = data.get("progress", "?")
                    print(f"  {i}. {company} — Day {day} | Progress {progress}%")

                print("\n  d. Delete a save")
                pick = input("\nEnter number or 'd': ").strip()

                if pick.lower() == "d":
                    del_pick = input("Enter number to delete: ").strip()
                    try:
                        del_index = int(del_pick) - 1
                        if 0 <= del_index < len(saves):
                            name = saves[del_index]
                            confirm = input(f"Delete '{name}'? (y/n): ").strip().lower()
                            if confirm == "y":
                                os.remove(name)
                                print("Save deleted.")
                            else:
                                print("Cancelled.")
                        else:
                            print("Invalid selection.")
                    except ValueError:
                        print("Invalid input.")
                    self.__init__()
                    self.show_intro()
                    return

                else:
                    try:
                        index = int(pick) - 1
                        if 0 <= index < len(saves):
                            self.load_game(saves[index])
                            print(f"\nWelcome back, {self.state.company_name}!")
                            print("=" * 50)
                            return
                        else:
                            print("Invalid selection. Starting new game.")
                    except ValueError:
                        print("Invalid input. Starting new game.")

        company = input("\nWhat is your startup called? ").strip()
        if not company:
            company = "Unnamed Startup"
        self.state.company_name = company

        print(f"\nWelcome, founder of {company}.")
        print("\nYOUR GOAL:")
        print("  Travel from San Jose to San Francisco,")
        print("  building and shipping your product along")
        print("  the way. Reach 100% progress to launch.")
        print("  Each 10% represents a real city milestone.")
        print("\nHOW TO WIN:")
        print("  Reach 100% progress before day 30.")
        print("\nHOW TO LOSE:")
        print("  - Cash hits $0       → startup shuts down")
        print("  - Morale hits 0      → team quits")
        print("  - Bugs reach 60      → users abandon you")
        print("  - Day 30 passes      → out of time")
        print("  - Hype > 80 + Bugs > 30 → public backlash")
        print("\nTIPS:")
        print("  - Work earns cash but burns morale")
        print("  - Travel moves you forward but adds bugs")
        print("  - Rest recovers morale but costs coffee")
        print("  - High hype + high bugs = public backlash")
        print("  - Check the weather before you travel")
        print("\nWEATHER EFFECTS:")
        print("  - Sunny  → morale +3, better travel odds")
        print("  - Cloudy → no effect")
        print("  - Rain   → progress -2, worse travel odds")
        print("  - Cold   → coffee drains faster")
        print("  - Heat   → morale and coffee drain")
        print("  - Storm  → bugs spike, morale drops")
        print("  - Fog    → slight progress penalty")
        print("=" * 50)

    def run(self):
        self.show_intro()
        while not self.state.game_over:
            condition, temp, city = get_weather(self.state.location_index)
            self.state.weather = condition

            self.display_status()

            if temp is not None:
                print(f"Today's weather in {city}: {condition} ({temp}°C)")
            else:
                print(f"Today's weather: {condition} (offline mode)")

            self.show_actions()
            self.apply_choice()

            if getattr(self.state, "free_action", False):
                self.state.free_action = False
                continue

            if getattr(self.state, "wants_save", False):
                self.save_game()
                self.state.wants_save = False
                print("\nReturning to menu...")
                self.state.game_over = True
                self.__init__()
                self.run()
                return

            end_day(self.state)

            if not self.state.game_over:
                self.state.day += 1
                self.save_game(silent=True)

    def save_game(self, silent=False):
        s = self.state
        filename = os.path.join("data", f"save_{s.company_name.replace(' ', '_')}.json")
        data = {
            "cash": s.cash,
            "morale": s.morale,
            "coffee": s.coffee,
            "bugs": s.bugs,
            "hype": s.hype,
            "progress": s.progress,
            "day": s.day,
            "location_index": s.location_index,
            "weather": s.weather,
            "company_name": s.company_name,
        }
        with open(filename, "w") as f:
            json.dump(data, f)
        if not silent:
            print("Game saved.")

    def load_game(self, filename):
        if not os.path.exists(filename):
            print("Save file not found.")
            return False
        with open(filename) as f:
            data = json.load(f)
        s = self.state
        for key, value in data.items():
            setattr(s, key, value)
        print("Game loaded.")
        return True
