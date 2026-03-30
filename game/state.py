class GameState:
    def __init__(self):
        self.cash = 10000
        self.morale = 100
        self.coffee = 50
        self.bugs = 0
        self.hype = 50
        self.progress = 0
        self.day = 1
        self.game_over = False
        self.weather = "clear"
        self.bought_coffee_today = False
        self.location_index = 0
        self.company_name = "Your Startup"
