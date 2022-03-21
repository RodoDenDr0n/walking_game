from termcolor import colored
import random


class Player:
    """Class representation for player"""
    def __init__(self, backpack, health=10, damage=1, protection=0,
                 weapon=None, armour=None, money=0, level=1, points=0):
        """
        Class representation of Player
        """
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
        """
        Function that destroys player's weapon, armour,
        empties points and backpack and resets level to 1
        """
        self.level = 1
        self.points = 0
        self.weapon = None
        self.armour = None
        self.backpack.clean()

    def set_default_stats(self):
        """
        Function that is responsible for clearing potion effects
        from player after battle
        """
        self.health = 10
        self.damage = 1 + self.weapon.damage if self.has_weapon() else 1
        self.protection = self.armour.protection if self.has_armour() else 0

    def battle_stats(self):
        """
        Returns string with boss health, damage and protection
        """
        stats = colored("Player's stats: ", "cyan", attrs=["bold"]) + \
            colored("\nhealth: ", "blue") + f"{self.health}" + \
            colored("\ndamage: ", "blue") + f"{self.damage}" + \
            colored("\nprotection: ", "blue") + f"{self.protection}"
        return stats

    def equip_weapon(self, weapon):
        """
        Function that is responsible for equipping weapon
        """
        self.unequip_weapon() if self.has_weapon() else None
        self.weapon = self.backpack.get_item(weapon)
        self.backpack.give_up_item(weapon)
        self.damage += self.weapon.damage

    def unequip_weapon(self):
        """
        Function that is responsible for unequipping weapon
        """
        self.damage -= self.weapon.damage
        self.backpack.add_item(self.weapon)
        self.weapon = None

    def equip_armour(self, armour):
        """
        Function that is responsible for equipping armour
        """
        self.unequip_armour() if self.has_armour() else None
        self.armour = self.backpack.get_item(armour)
        self.backpack.give_up_item(armour)
        self.protection += self.armour.protection

    def unequip_armour(self):
        """
        Function that is responsible for unequipping armour
        """
        self.damage -= self.armour.protection
        self.backpack.add_item(self.armour)
        self.armour = None

    def has_weapon(self):
        """
        Function that is responsible for
        checking if player has weapon
        """
        if self.weapon is not None:
            return True
        return False

    def has_armour(self):
        """
        Function that is responsible for
        checking if player has armour
        """
        if self.armour is not None:
            return True
        return False

    def level_up(self):
        """
        Function that is responsible for leveling up
        """
        if self.level < 8:
            self.level += 1
            print(colored("You have leveled up!", "green", attrs=["bold"]))
        else:
            pass

    def get_loot(self, items):
        """
        Function that is responsible for player to get loot
        """
        amount = random.choice([1, 1, 2, 2, 2, 3])
        for i in range(amount):
            self.backpack.add_item(random.choice(items))

    def add_points(self):
        """
        Function that is responsible for player to get points
        """
        amount = random.choice([1, 1, 1, 2, 2, 2, 2, 3, 3])
        self.points += amount
        if self.points >= 20:
            self.points = 0
            self.level_up()

    def __str__(self):
        """
        String representation of class Player
        """
        return colored("\nPlayer Stats:", "red", attrs=["bold"]) + \
            colored("\nHealth", "green") + f": {self.health}" + \
            colored("\nDamage", "green") + f": {self.damage}" + \
            colored("\nProtection", "green") + f": {self.protection}" + \
            colored("\nCurrent weapon", "green") + f": {self.weapon}" + \
            colored("\nCurrent armour", "green") + f": {self.armour}" + \
            colored("\nMoney", "green") + f": {self.money}" + \
            colored("\nLevel", "green") + f": {self.level}" + \
            colored("\nPoints", "green") + f": {self.points}"


class Backpack:
    """Class representation for backpack"""
    def __init__(self, equipment=None):
        """
        Creates Backpack
        """
        self.equipment = equipment or {}

    def add_item(self, item):
        """
        Function that is responsible for adding item to backpack
        """
        if item in self.equipment.keys():
            self.equipment[item] += 1
        else:
            self.equipment.setdefault(item, 1)

    def get_item(self, item_name):
        """
        Function that is responsible for getting item from backpack
        """
        for item in self.equipment:
            if item.name == item_name:
                return item
        return colored("No such item!", "red", attrs=["bold"])

    def give_up_item(self, destroy_item):
        """
        Function that is responsible for deleting item from backpack
        """
        for item in self.equipment.keys():
            if item.name == destroy_item:
                self.equipment[item] -= 1
                if self.equipment[item] == 0:
                    self.equipment.pop(item)
                break

    def sell_item(self, item, other):
        """
        Function that is responsible for selling item from backpack
        """
        if item in self.equipment.keys():
            self.equipment[item] -= 1
            other.money += item.price
            if self.equipment[item] == 0:
                self.equipment.pop(item)

    def clean(self):
        """
        Function that is responsible for cleaning backpack
        """
        self.equipment = {}

    def __str__(self):
        """
        String representation of class Backpack
        """
        string = colored("\nYour items:", "red", attrs=["bold"])
        for item, count in self.equipment.items():
            string += str(item)
            string += colored("\n  Amount: ", "blue") + colored(f"x{count}", attrs=["bold"])
        return string


class Shop:
    """Class representation for shop"""
    def __init__(self, backpack, game_player, items_for_sale):
        """
        Creates shop
        """
        self.backpack = backpack
        self.game_player = game_player
        self.items_for_sale = items_for_sale

    def sell(self):
        """
        Function responsible for selling items
        """
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
        """
        Function responsible for buying items
        """
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
        """
        Function responsible for getting command
        """
        command = input("Enter command:" + colored("\n>>> ", "red", attrs=["bold"]))
        return command

    def __str__(self):
        """
        String representation of shop
        """
        shopping = colored("\nMoney:", "cyan", attrs=["bold"]) + f" {self.game_player.money}" + \
            colored("\nBuy boosters:", "red", attrs=["bold"])
        for item in self.items_for_sale:
            shopping += str(item)
        return shopping
