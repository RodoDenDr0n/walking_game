from termcolor import colored


class Location:
    def __init__(self, name, number, map=None, shop=False, boss=False, linked=None):
        self.name = name
        self.number = number
        self.map = map or []
        self.shop = shop
        self.boss = boss
        self.linked = linked or {}

    def plant_boss(self, boss):
        self.boss = boss

    def add_shop(self):
        self.shop = True

    def move(self, user_direction):
        for linked_direction, location_number in self.linked.items():
            if linked_direction == user_direction:
                return location_number

    def __str__(self):
        return f"Location({self.name}, {self.number}, " \
               f"boss={self.boss}, shop={self.shop}, linked={self.linked})"

    def __repr__(self):
        return f"Location({self.name}, {self.number}, " \
               f"boss={self.boss}, shop={self.shop}, linked={self.linked})"


class Compass:
    def __str__(self):
        compass = """
    >=====<Compass>=====<
    |       north       |
    |         !         |
    | west --   -- east |
    |         ¡         |
    |       south       |
    >===================<
            """
        colored_elements = {"cyan":[">", "<"], "grey":["=", "|"], "red":["-", "!", "¡"],
                            "magenta":["Compass"], "blue":["north", "east", "south", "west"]}
        for key, values in colored_elements.items():
            for element in values:
                elements_number = compass.count(element)
                compass = compass.replace(element, colored(element, key, attrs=["bold"]), elements_number)
        return compass


class Map:
    def __init__(self, map):
        self.map = map

    def __str__(self):
        colored_elements = {"cyan":[">", "<", "*"], "grey":["=", "|"], "green":["-", "!", "¡"],
                            "magenta":["Map", "B", "S"], "blue":["(", ")"], "red":["@"]}
        for key, values in colored_elements.items():
            for element in values:
                elements_number = self.map.count(element)
                self.map = self.map.replace(element, colored(element, key, attrs=["bold"]), elements_number)
        return self.map
