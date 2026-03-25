# Silicon Trail

Silicon Trail is a terminal-based strategy and resource management game written in Python. The player manages a startup on a journey to San Francisco, balancing resources, team morale, product quality, and market hype in order to successfully launch.

---

## Overview

Each turn represents a day. Players choose actions that impact multiple aspects of their startup. The goal is to reach 100% progress (arrival in San Francisco) without running out of resources or collapsing due to poor decisions.

The game emphasizes trade-offs, risk management, and strategic planning.

---

## Features

* Modular, object-oriented design
* Turn-based gameplay loop
* Resource management system:

  * Cash
  * Morale
  * Coffee
  * Bugs
  * Hype
  * Progress
* Action system using class-based design
* Random events and dynamic outcomes
* Weather system with API-ready structure and fallback
* Input validation (prevents invalid turns)
* Multiple win and loss conditions

---

## Project Structure

```
silicon_trail/
├── main.py
├── api/
│   └── weather.py
├── game/
│   ├── engine.py
│   ├── state.py
│   ├── events.py
│   └── actions/
│       ├── base.py
│       ├── travel.py
│       ├── rest.py
│       ├── work.py
│       ├── market.py
│       └── buy_coffee.py
└── tests/
```

---

## How to Run

1. Clone the repository or download the files

2. Navigate to the project directory:

```
cd silicon_trail
```

3. Run the game:

```
python3 main.py
```

---

## Gameplay

Each day:

1. Your current stats are displayed
2. You choose an action
3. The action updates your resources
4. Random events and weather effects occur
5. The game checks for win or loss conditions

---

## Actions

* Travel
  Progress toward your goal, but costs resources and may introduce bugs

* Rest
  Recovers morale, but may allow bugs to accumulate

* Work
  Fixes bugs, but reduces morale and consumes coffee

* Marketing
  Increases hype, but costs money and can introduce bugs

* Buy Coffee
  Converts cash into coffee to sustain future actions

---

## Game Mechanics

Every action has trade-offs. For example:

* Increasing hype without fixing bugs can lead to failure
* Working too much reduces morale
* Traveling too aggressively can introduce instability

Randomness is used to simulate real-world uncertainty.

---

## Win Condition

* Reach 100% progress (successfully launch in San Francisco)

---

## Loss Conditions

* Cash reaches 0 (bankruptcy)
* Morale reaches 0 (team burnout)
* Bugs exceed threshold (product failure)
* High hype + high bugs (public backlash)

---

## Weather System

The game includes a weather system that:

* Affects gameplay each turn
* Uses a fallback random generator
* Is designed to support real API integration in the future

---

## Future Improvements

* Convert events into class-based system (like actions)
* Integrate real weather API
* Add difficulty levels
* Introduce new actions (hire, pivot, invest)
* Add save/load functionality
* Expand event system with conditional triggers

---

## Design Goals

* Clean, modular architecture
* Separation of concerns (game logic vs external data)
* Extensibility for future features
* Maintainable and readable code

---

## Author

Luis Gomez

---

## Notes

This project was built to explore:

* Object-oriented design in Python
* Game loop architecture
* Resource balancing and system design
* Basic API integration patterns

