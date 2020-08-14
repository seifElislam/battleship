"""
Ship module
"""


class Ship:
    """
    Ship class
    """
    def __init__(self, areas):
        """

        :param areas:
        """
        self.head = None
        self.status = 1
        self.add_areas(areas)

    def add_areas(self, areas):
        """

        :param areas:
        :return:
        """
        for area in areas:
            if area.next or area.get_belong_to_ship():
                raise Exception('Two shipments overlap')
            area.set_belong_to_ship()
            ptr1 = area
            temp = self.head

            ptr1.next = self.head

            # If linked list is not None then set the next of
            # last node
            if self.head is not None:
                while temp.next != self.head:
                    temp = temp.next
                temp.next = ptr1

            else:
                ptr1.next = ptr1  # For the first node

            self.head = ptr1

    def check_status(self):
        """

        :return:
        """
        pass