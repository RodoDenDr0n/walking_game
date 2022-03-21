import json
import random
from termcolor import colored


class Enemy:
    """Class representation for enemy"""
    def __init__(self, health=None, damage=None, protection=None):
        self.health = health
        self.damage = damage
        self.protection = protection

    @staticmethod
    def spawn(level, file):
        """
        Spawns the enemy
        """
        with open(file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            for key in data.keys():
                if int(key) == level:
                    minimum_health = data[key]["health"][0]
                    maximum_health = data[key]["health"][1]
                    health = random.choice(range(minimum_health, maximum_health))
                    minimum_damage = data[key]["damage"][0]
                    maximum_damage = data[key]["damage"][1]
                    damage = random.choice(range(minimum_damage, maximum_damage))
                    minimum_protection = data[key]["protection"][0]
                    maximum_protection = data[key]["protection"][1]
                    protection = random.choice(range(minimum_protection, maximum_protection))
                    return Enemy(health, damage, protection)

    def battle_stats(self):
        """
        Returns string with enemy's health, damage and protection
        """
        stats = colored("\nEnemy's stats: ", "cyan", attrs=["bold"]) + \
            colored("\nhealth: ", "blue") + f"{self.health}" + \
            colored("\ndamage: ", "blue") + f"{self.damage}" + \
            colored("\nprotection: ", "blue") + f"{self.protection}"
        return stats


class Boss(Enemy):
    """Class representation for boss enemy"""

    def battle_stats(self):
        """
        Returns string with boss health, damage and protection
        """
        stats = colored("\nBoss stats: ", "cyan", attrs=["bold"]) + \
            colored("\nhealth: ", "blue") + f"{self.health}" + \
            colored("\ndamage: ", "blue") + f"{self.damage}" + \
            colored("\nprotection: ", "blue") + f"{self.protection}"
        return stats


class Battle:
    """Class for battle representation"""
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    @staticmethod
    def command_options():
        """
        Function that prints command options to use in battle
        """
        selector = colored(" [+] ", "green")
        print(colored("\nYour action:", "cyan", attrs=["bold"]))
        print(selector + "backpack")
        print(selector + "damage")

    def player_turn(self):
        """
        Function that is called for player to make his turn
        """
        print(colored("\nYour turn!", "red", attrs=["bold"]))
        print(self.player.battle_stats())
        print(self.enemy.battle_stats())
        self.command_options()
        command = input(colored(">>> ", "red", attrs=["bold"]))
        if command == "backpack":
            self.open_backpack()
            return self.player_turn()
        elif command == "damage":
            self.deal_damage()
            return None
        else:
            print(colored("No such command!", "red", attrs=["bold"]))
            return self.player_turn()

    def open_backpack(self):
        """
        Function that is called if player decides to open backpack in battle
        """
        available_potions = []
        print(colored("\nYour potions:", "red", attrs=["bold"]))
        for element in self.player.backpack.equipment:
            if "potion" in element.name:
                available_potions.append(element.name)
                print(colored(" [+] ", "green") + colored(element.name, "magenta"))
        print(colored(" [+] ", "green") + colored("finish", "magenta"))
        self.choose_potion()

    def choose_potion(self):
        """
        Function that is responsible for letting player choose the potion
        """
        potions_message = "Choose " + colored("the potion", "green") + \
                          " you want to use:" + colored("\n>>> ", "red", attrs=["bold"])
        desired_potion = input(potions_message)
        if desired_potion == "bear potion":
            self.player.damage += round(0.5 * (10 - self.player.health))
            self.player.backpack.give_up_item(desired_potion)
            self.open_backpack()
        elif desired_potion == "porcupine potion":
            self.player.protection += round(0.5 * (10 - self.player.health))
            self.player.backpack.give_up_item(desired_potion)
            self.open_backpack()
        elif desired_potion == "healing potion":
            self.player.health += 3
            self.player.backpack.give_up_item(desired_potion)
            self.open_backpack()
        elif desired_potion == "finish":
            print(colored("Time to fight!", "red", attrs=["bold"]))
        else:
            print(colored("No such potion!", "red", attrs=["bold"]))

    def deal_damage(self):
        """
        Function that deals damage to enemy
        """
        self.enemy.health -= self.player.damage - self.enemy.protection
        if self.player.has_weapon():
            self.enemy.health -= self.player.weapon.damage

    def enemy_turn(self):
        """
        Function that is called for enemy to make his turn
        """
        print(colored("\nEnemy's turn!", "red", attrs=["bold"]))
        self.player.health -= self.enemy.damage - self.player.protection
        print("Enemy deals " + colored(f"{self.enemy.damage}", "red") + " damage!")

    def fight(self):
        """
        Function which has the main battle cycle
        """
        while True:
            self.player_turn()
            if self.enemy.health <= 0:
                return True
            self.enemy_turn()
            if self.player.health <= 0:
                return False
