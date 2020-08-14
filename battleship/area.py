"""
Area module
"""


class Area:
    """
    Area class
    """
    def __init__(self, x_coordinate, y_coordinate, status=1, next=None):
        """

        :param x_coordinate:
        :param y_coordinate:
        :param status:
        :param next:
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self._status = status
        self.next = next
        self._belong_to_ship = False

    def get_status(self):
        """

        :return:
        """
        return self._status

    def set_status(self, status):
        """

        :param status:
        :return:
        """
        self._status = status

    def get_belong_to_ship(self):
        """

        :return:
        """
        return self._belong_to_ship

    def set_belong_to_ship(self):
        """

        :return:
        """
        self._belong_to_ship = True

    def __repr__(self):
        """

        :return:
        """
        return '({}, {})'.format(self.x_coordinate, self.y_coordinate)

