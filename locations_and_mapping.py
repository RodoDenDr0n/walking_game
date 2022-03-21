from termcolor import colored


class Location:
    """Class representation for Location"""
    def __init__(self, name, number, map=None, shop=False, boss=False, linked=None):
        self.name = name
        self.number = number
        self.map = map or []
        self.shop = shop
        self.boss = boss
        self.linked = linked or {}

    def move(self, user_direction):
        """
        Function that is responsible for returning location number
        """
        for linked_direction, location_number in self.linked.items():
            if linked_direction == user_direction:
                return location_number

    def __str__(self):
        """
        String representation of Location class
        """
        selector = colored("\n [+] ", "green")
        string = colored("\nLocation information:", "cyan")
        string += selector + colored("location name: ") + self.name
        string += selector + colored("location number: ") + f"{self.number}"
        if self.shop:
            string += colored("\nLocation has shop", "magenta")
        else:
            string += colored("\nLocation has no shop", "white")
        if self.boss:
            string += colored("\nThere is boss in this location that needs to be defeated!", "red")
        else:
            string += colored("\nThere is no boss in this location", "white")

        return string


class Compass:
    def __str__(self):
        """
        String representation for Compass class
        """
        compass = """
    >=====<Compass>=====<
    |       north       |
    |         !         |
    | west --   -- east |
    |         ¡         |
    |       south       |
    >===================<
            """
        colored_elements = {"cyan": [">", "<"], "grey": ["=", "|"], "red": ["-", "!", "¡"],
                            "magenta": ["Compass"], "blue": ["north", "east", "south", "west"]}
        for key, values in colored_elements.items():
            for element in values:
                elements_number = compass.count(element)
                compass = compass.replace(element, colored(element, key, attrs=["bold"]), elements_number)
        return compass


class Map:
    """Class for Map representation"""
    def __init__(self, map):
        self.map = map

    def __str__(self):
        """
        String representation for map
        """
        colored_elements = {"cyan": [">", "<", "*"], "grey": ["=", "|"], "green": ["-", "!", "¡"],
                            "magenta": ["Map", "B", "S"], "blue": ["(", ")"], "red": ["@"]}
        for key, values in colored_elements.items():
            for element in values:
                elements_number = self.map.count(element)
                self.map = self.map.replace(element, colored(element, key, attrs=["bold"]), elements_number)
        return self.map
