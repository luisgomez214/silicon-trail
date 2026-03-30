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

## Demo
[Watch Video](https://github.com/luisgomez214/silicon-trail/blob/main/Screen%20Recording%202026-03-30%20at%2012.24.16%E2%80%AFAM.mov)
