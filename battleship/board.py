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

        :param size: tuple (10, 10)
        """
        self.size = size
        self.areas = self.init_area(self.size)
        self.ships = []

    def init_area(self, size):
        """

        :param size:
        :return:
        """
        areas = []
        for x in range(size[0]):
            for y in range(size[1]):
                assert x <= self.size[0], "Invalid x coordinate."
                assert y <= self.size[1], "Invalid x coordinate."
                areas.append(Area(x, y))
        return areas

    def add_ship(self, x, y, size, direction):
        """

        :param x:
        :param y:
        :param size:
        :param direction:
        :return:
        """
        new_ship_area = self.find_ship_area(x, y, size, direction)
        self.areas += new_ship_area
        self.ships.append(Ship(new_ship_area))

    def find_coordinate(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        new_area = None
        for area in self.areas:
            if area.x_coordinate == x and area.y_coordinate == y:
                new_area = area
        if not new_area:
            raise Exception('a ship falls beyond the size of the board.')
        return new_area

    def find_ship_area(self, x, y, size, direction):
        """

        :param x:
        :param y:
        :param size:
        :param direction:
        :return:
        """
        areas = []
        new_x = x
        new_y = y
        for i in range(size):
            if direction == 'H':
                new_x = x + i
                new_y = y
            elif direction == 'V':
                new_x = x
                new_y = y + i

            assert new_x <= self.size[0], "a ship falls beyond the size of the board."
            assert new_y <= self.size[1], "a ship falls beyond the size of the board."

            areas.append(self.find_coordinate(new_x, new_y))
        return areas

    def handle_shot(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        assert x <= self.size[0]
        assert y <= self.size[1]
        hit_area = None
        for area in self.areas:
            if area.x_coordinate == x and area.y_coordinate == y:
                area.set_status(0)
                hit_area = area
                break

        if not hit_area:
            hit_area = Area(x, y, 0)
            self.areas.append(hit_area)

        sink_flag = True
        temp_area = hit_area
        if temp_area.get_belong_to_ship():
            while temp_area.next:
                if temp_area.next == hit_area:
                    break
                if temp_area.next.get_status() == 1:
                    sink_flag = False
                    break
                temp_area = temp_area.next
        else:
            sink_flag = False
        status = 'HIT' if hit_area.get_belong_to_ship() else 'WATER'
        return 'SINK' if sink_flag else status
