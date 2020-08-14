"""
Game module
"""
from battleship.board import Board


class Game:
    """

    """
    __instance__ = None

    def __init__(self, board_size):
        """

        :param board_size:
        """
        if Game.__instance__ is None:
            Game.__instance__ = self
            self.board = Board(board_size)

    @staticmethod
    def get_instance(size):
        """ Static method to fetch the current instance.
        """
        if not Game.__instance__:
            Game(size)
        return Game.__instance__

    def add_ship(self, x, y, size, direction):
        """

        :param x:
        :param y:
        :param size:
        :param direction:
        :return:
        """
        self.board.add_ship(x, y, size, direction)

    def handle_shot(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        return self.board.handle_shot(x, y)
