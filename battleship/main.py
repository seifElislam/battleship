from battleship.game import Game
from battleship.board import Board
from battleship.ship import Ship
from battleship.area import Area


if __name__ == '__main__':
    g = Game((10, 10))
    g.add_ship(6, 7, 1, 'H')
    g.add_ship(3, 5, 5, 'V')
    g.add_ship(5, 5, 4, 'H')
    g.add_ship(6, 6, 3, 'V')


