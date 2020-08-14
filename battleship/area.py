"""
Area module
"""


class Area:
    """
    Area class
    """
    def __init__(self, x_coordinate, y_coordinate, next=None):
        """

        :param x_coordinate:
        :param y_coordinate:
        :param next:
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.status = 1
        self.next = next
