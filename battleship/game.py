"""
Game module
"""
from battleship.board import Board


class Game:
    """

    """
    def __init__(self, board_size):
        """

        :param board_size:
        """
        self.board = Board(board_size)

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
