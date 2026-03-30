from game.actions.travel import Travel
from game.actions.rest import Rest
from game.actions.work import Work
from game.actions.market import Market
from game.actions.buy_coffee import BuyCoffee
from game.actions.save import Save

ACTIONS = [
    Travel(),
    Rest(),
    Work(),
    Market(),
    BuyCoffee(),
    Save(),
]
