"""
Board module
"""
from battleship.area import Area
from battleship.ship import Ship


class Board:
    """

    """
    def __init__(self, size):
        """

        :param size:
        """
        self.areas = self.init_areas(size)
        self.ships = []

    def init_areas(self, size):
        """

        :param size:
        :return:
        """
        pass

    def add_ship(self, ship):
        """

        :param ship:
        :return:
        """
        self.ships.append(ship)
