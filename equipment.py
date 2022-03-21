from termcolor import colored


class Item:
    """Class for Item representation"""
    def __init__(self, name, damage, protection, description, price):
        self.name = name
        self.damage = damage
        self.protection = protection
        self.description = description
        self.price = price


class Weaponry(Item):
    """Class for Weaponry representation"""
    def __init__(self, name, damage, protection, price):
        super().__init__(name, damage, protection, None, price)

    def __str__(self):
        """
        String class representation
        """
        return colored("\n [+] ", "green") + \
            colored(f"{self.name}:", "magenta") + \
            "\n  - " + colored("damage:", "cyan") + f" {self.damage}" + \
            "\n  - " + colored("protection:", "cyan") + f" {self.protection}" + \
            "\n  - " + colored("price:", "cyan") + f" {self.price}"


class Weapon(Weaponry):
    """Class for Weapon representation"""
    def __init__(self, name, damage, price):
        super().__init__(name, damage, None, price)

    def __str__(self):
        return colored("\n [+] ", "green") + \
              colored(f"{self.name}:", "magenta") + \
              "\n  - " + colored("damage:", "cyan") + f" {self.damage}" + \
              "\n  - " + colored("price:", "cyan") + f" {self.price}"


class Armour(Weaponry):
    """Class for Armour representation"""
    def __init__(self, name, protection, price):
        super().__init__(name, None, protection, price)

    def __str__(self):
        return colored("\n [+] ", "green") + \
              colored(f"{self.name}:", "magenta") + \
              "\n  - " + colored("protection:", "cyan") + f" {self.protection}" + \
              "\n  - " + colored("price:", "cyan") + f" {self.price}"


class Potion(Item):
    """Class for Potion representation"""
    def __init__(self, name, description, price):
        super().__init__(name, None, None, description, price)

    def __str__(self):
        """
        String representation for potion class
        """
        return colored("\n [+] ", "green") + colored(f"{self.name}", "magenta") + \
            colored(f" ({self.price} coins)", "cyan") + colored(f":", "magenta") + \
            f" {self.description}"
