from termcolor import colored
import random


class Player:
    def __init__(self, backpack, health=10, damage=1, protection = 0,
                 weapon=None, armour=None, money=1000, level=1, points=0):
        self.health = health
        self.damage = damage
        self.protection = protection
        self.weapon = weapon
        self.armour = armour
        self.backpack = backpack
        self.money = money
        self.level = level
        self.points = points

    def clean(self):
        self.weapon = None
        self.armour = None
        self.level = 1
        self.backpack.clean()

    def set_default_stats(self):
        self.health = 10
        self.damage = 1 + self.weapon.damage if self.has_weapon() else 1
        self.protection = self.armour.protection if self.has_armour() else 0

    def battle_stats(self):
        stats = colored("Player's stats: ", "cyan", attrs=["bold"]) + \
                 colored("\nhealth: ", "blue") + f"{self.health}" + \
                 colored("\ndamage: ", "blue") + f"{self.damage}" + \
                 colored("\nprotection: ", "blue") + f"{self.protection}"
        return stats

    def equip_weapon(self, weapon):
        self.unequip_weapon() if not self.has_weapon() else None
        self.backpack.give_up_item(weapon)
        self.weapon = self.backpack.get_item(weapon)
        self.damage += self.weapon.damage

    def unequip_weapon(self):
        self.damage -= self.weapon.damage
        self.backpack.add_item(self.weapon)
        self.weapon = None

    def equip_armour(self, armour):
        self.unequip_armour() if not self.has_armour() else None
        self.backpack.give_up_item(armour)
        self.armour = self.backpack.get_item(armour)
        self.protection += self.armour.protection

    def unequip_armour(self):
        self.damage -= self.armour.protection
        self.backpack.add_item(self.armour)
        self.armour = None

    def has_weapon(self):
        if self.weapon is not None:
            return True
        return False

    def has_armour(self):
        if self.armour is not None:
            return True
        return False

    def level_up(self):
        self.level += 1

    def get_loot(self, items):
        amount = random.choice([1, 1, 2, 2, 2, 3])
        for i in range(amount):
            self.backpack.add_item(random.choice(items))

    def __str__(self):
        return colored("\nPlayer Stats:", "red", attrs=["bold"]) + \
               colored("\nHealth", "green") + f": {self.health}" + \
               colored("\nDamage", "green") + f": {self.damage}" + \
               colored("\nProtection", "green") + f": {self.protection}" + \
               colored("\nCurrent weapon", "green") + f": {self.weapon}" + \
               colored("\nCurrent armour", "green") + f": {self.armour}" + \
               colored("\nMoney", "green") + f": {self.money}" + \
               colored("\nLevel", "green") + f": {self.level}"


class Backpack:
    def __init__(self, equipment=None):
        self.equipment = equipment or {}

    def add_item(self, item):
        if item in self.equipment.keys():
            self.equipment[item] += 1
        else:
            self.equipment.setdefault(item, 1)

    def get_item(self, item_name):
        for item in self.equipment:
            if item.name == item_name:
                return item
        return colored("No such item!", "red", attrs=["bold"])

    def give_up_item(self, item):
        if item in self.equipment.keys():
            self.equipment[item] -= 1
            if self.equipment[item] == 0:
                self.equipment.pop(item)

    def sell_item(self, item, other):
        if item in self.equipment.keys():
            self.equipment[item] -= 1
            other.money += item.price
            if self.equipment[item] == 0:
                self.equipment.pop(item)

    def clean(self):
        self.equipment = {}

    def __str__(self):
        string = colored("\nYour items:", "red", attrs=["bold"])
        for item, count in self.equipment.items():
            string += str(item)
            string += colored("\n  Amount", "blue") + ": " + colored(f"x{count}", attrs=["bold"])
        return string

    def __repr__(self):
        return f"{self.equipment}"


class Shop:
    def __init__(self, backpack, game_player, items_for_sale):
        self.backpack = backpack
        self.game_player = game_player
        self.items_for_sale = items_for_sale

    def sell(self):
        print(self.backpack)
        item_for_sale = input("Enter the item " +
                              colored("for sale", "green") + ":" +
                              colored("\n>>> ", "red", attrs=["bold"]))
        if item_for_sale == "finish":
            return colored("You exited shop", "red", attrs=["bold"])
        for item in self.backpack.equipment:
            if item.name == item_for_sale:
                self.backpack.sell_item(item, self.game_player)
                print(colored("Item sold!", "green", attrs=["bold"]))
                return self.sell()
        print(colored("There is no such item!", "red", attrs=["bold"]))
        return self.sell()

    def buy(self):
        print(self)
        item_to_buy = input("Enter the item " +
                              colored("to buy", "green") + ":" +
                              colored("\n>>> ", "red", attrs=["bold"]))
        if item_to_buy == "finish":
            return colored("You exited shop", "red", attrs=["bold"])
        for item in self.items_for_sale:
            if item.name == item_to_buy:
                if item.price > self.game_player.money:
                    print(colored("You don't have enough money!", "red", attrs=["bold"]))
                    return self.buy()
                self.game_player.money -= item.price
                self.backpack.add_item(item)
                print(colored("Item added to your backpack!", "green", attrs=["bold"]))
                return self.buy()
        print(colored("There is no such item!", "red", attrs=["bold"]))
        return self.buy()

    @staticmethod
    def enter_command():
        command = input("Enter command:" + colored("\n>>> ", "red", attrs=["bold"]))
        return command

    def __str__(self):
        shopping = colored("\nMoney:", "cyan", attrs=["bold"]) + f" {self.game_player.money}" + \
                 colored("\nBuy boosters:", "red", attrs=["bold"])
        for item in self.items_for_sale:
            shopping += str(item)
        return shopping
