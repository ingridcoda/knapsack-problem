class Item:
    def __init__(self, size, value):
        self.size = size
        self.value = value

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return self.__str__()


class Knapsack:
    def __init__(self, size=0, items=None):
        self.size = size
        self.items = []
        if items:
            self.items = items

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return self.__str__()

    def get_total_value(self):
        return sum([item.value for item in self.items])






