from termcolor import colored


class Item:
    def __init__(self, name, damage, protection, description, price):
        self.name = name
        self.damage = damage
        self.protection = protection
        self.description = description
        self.price = price


class Weaponry(Item):
    def __init__(self, name, damage, protection, price):
        super().__init__(name, damage, protection, None, price)

    def __str__(self):
        return colored("\n [+] ", "green") + \
              colored(f"{self.name}:", "magenta") + \
              "\n  - " + colored("damage:", "cyan") + f" {self.damage}" + \
              "\n  - " + colored("protection:", "cyan") + f" {self.protection}" + \
              "\n  - " + colored("price:", "cyan") + f" {self.price}"

    def __repr__(self):
        return f"{self.name}=(dmg: {self.damage}, prtc: {self.protection})"


class Weapon(Weaponry):
    def __init__(self, name, damage, price):
        super().__init__(name, damage, None, price)

    def __str__(self):
        return colored("\n [+] ", "green") + \
              colored(f"{self.name}:", "magenta") + \
              "\n  - " + colored("damage:", "cyan") + f" {self.damage}" + \
              "\n  - " + colored("price:", "cyan") + f" {self.price}"

class Armour(Weaponry):
    def __init__(self, name, protection, price):
        super().__init__(name, None, protection, price)

    def __str__(self):
        return colored("\n [+] ", "green") + \
              colored(f"{self.name}:", "magenta") + \
              "\n  - " + colored("protection:", "cyan") + f" {self.protection}" + \
              "\n  - " + colored("price:", "cyan") + f" {self.price}"


class Potion(Item):
    def __init__(self, name, description, price):
        super().__init__(name, None, None, description, price)

    def __str__(self):
        return colored("\n [+] ", "green") + colored(f"{self.name}", "magenta") + \
               colored(f" ({self.price} coins)", "cyan") + colored(f":", "magenta") + \
               f" {self.description}"

    def __repr__(self):
        return f"{self.name}=(price: {self.price} coins)"
