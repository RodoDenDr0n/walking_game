from player import Player, Backpack, Shop
from generator import ItemGenerator, MapGenerator
from termcolor import colored
from locations_and_mapping import Compass, Map
from enemies import Enemy, Boss, Battle
from equipment import Weapon, Armour

backpack = Backpack()
game_player = Player(backpack)

item_generator = ItemGenerator()
item_generator.generate_objects("items.json")  # generates dictionary with key:level, value:items list
map = MapGenerator()
map.generate_objects("map.json")  # generates list of locations
locations = map.generated

shop = Shop(backpack, game_player, item_generator.generated["potions"])


class Game:
    """Class representation for Game"""
    def __init__(self, shop, current_location, locations, player, defeated_bosses=0):
        """
        Creates Game
        """
        self.item_generator = item_generator
        self.shop = shop
        self.current_location = current_location
        self.locations = locations
        self.player = player
        self.defeated_bosses = defeated_bosses

    def run(self):
        """
        Function that runs the game
        """
        command = input("Enter the " + colored("command", "green") + ":" +
                        colored("\n>>> ", "red", attrs=["bold"]))

        if command == "sell":
            if self.current_location.shop:
                return self.shop.sell()
            return colored("There is no shop in this location!", "red", attrs=["bold"])

        elif command == "buy":
            if self.current_location.shop:
                return self.shop.buy()
            return colored("There is no shop in this location!", "red", attrs=["bold"])

        elif command == "backpack":
            return str(self.player.backpack)

        elif command == "me":
            return str(self.player)

        elif command == "move":
            current_location_map = "\n".join(self.current_location.map)
            print(Map(current_location_map))
            print(Compass())
            direction = input("Enter the direction you want " +
                              colored("to move:", "green") +
                              colored("\n>>> ", "red", attrs=["bold"]))
            number = self.current_location.move(direction)
            for location in locations:
                if location.number == number:
                    self.current_location = location
                    return colored(f"You moved {direction}", "green", attrs=["bold"])
            return colored(f"You can't go {direction}", "red", attrs=["bold"])

        elif command == "map":
            current_location_map = "\n".join(self.current_location.map)
            return Map(current_location_map)

        elif command == "location":
            return self.current_location

        elif command == "fight":
            if self.current_location.boss is True:
                if self.player.level in [3, 5, 7]:
                    enemy = Boss.spawn(self.defeated_bosses, "bosses.json")
                    enemy_type = "boss"
                else:
                    return colored("Your level is to low to fight with boss!", "red", attrs=["bold"])
            else:
                enemy = Enemy.spawn(game_player.level, "enemies.json")
                enemy_type = "common"

            result = Battle(game_player, enemy).fight()
            if result:
                game_player.set_default_stats()
                level_items = item_generator.generated[game_player.level]

                if enemy_type == "common":
                    game_player.add_points()
                elif enemy_type == "boss":
                    game_player.level_up()
                    self.defeated_bosses += 1
                    self.current_location.boss = False
                game_player.get_loot(level_items)
                return colored("You win!", "green", attrs=["bold"])

            game_player.set_default_stats()
            game_player.clean()
            return colored("You lost all your items and level!", "red", attrs=["bold"])

        elif command == "equip":
            equipment_proposal = colored("\nWhat do you want to equip?", "cyan") + \
                colored("\n [+] ", "green") + "weapon" + \
                colored("\n [+] ", "green") + "armour" + \
                colored("\n>>> ", "red", attrs=["bold"])
            desired_equipment = input(equipment_proposal)

            equipment_type = None
            if desired_equipment == "weapon":
                equipment_type = Weapon
            elif desired_equipment == "armour":
                equipment_type = Armour

            message = colored(f"\nYour {desired_equipment} pieces:", "red", attrs=["bold"])
            for element in self.player.backpack.equipment:
                if isinstance(element, equipment_type):
                    message += str(element)
            print(message)

            chosen_equipment = input(colored("Equip: ", "red", attrs=["bold"]))
            if equipment_type == Weapon:
                game_player.equip_weapon(chosen_equipment)
            elif equipment_type == Armour:
                game_player.equip_armour(chosen_equipment)
            return colored(f"You equipped {chosen_equipment}!", "green", attrs=["bold"])

        elif command == "unequip":
            equipment_proposal = colored("\nWhat do you want to unequip?", "cyan") + \
                colored("\n [+] ", "green") + "weapon" + \
                colored("\n [+] ", "green") + "armour" + \
                colored("\n>>> ", "red", attrs=["bold"])
            desired_equipment = input(equipment_proposal)

            if desired_equipment == "weapon":
                game_player.unequip_weapon()
            elif desired_equipment == "armour":
                game_player.unequip_weapon()

        else:
            return colored("No such command!", "red", attrs=["bold"])

    def __str__(self):
        """
        String representation for class Game
        """
        selector = colored("\n [+] ", "green")
        possible_commands = colored("\nPossible actions:", "cyan", attrs=["bold"]) + \
            selector + "backpack" + \
            selector + "me" + \
            selector + "move" + \
            selector + "map" + \
            selector + "location" + \
            selector + "fight" + \
            selector + "equip" + \
            selector + "unequip"
        if self.current_location.shop:
            possible_commands += selector + "sell" + \
                                selector + "buy"
        return possible_commands


class GameCover:
    """Class representation of Game Cover"""
    def __str__(self):
        """
        String representation of class
        """
        cover = \
            """
         ██╗       ██╗ █████╗ ███╗  ██╗██████╗ ███████╗██████╗    █████╗ ███╗  ██╗██████╗ 
         ██║  ██╗  ██║██╔══██╗████╗ ██║██╔══██╗██╔════╝██╔══██╗  ██╔══██╗████╗ ██║██╔══██╗
         ╚██╗████╗██╔╝███████║██╔██╗██║██║  ██║█████╗  ██████╔╝  ███████║██╔██╗██║██║  ██║
          ████╔═████║ ██╔══██║██║╚████║██║  ██║██╔══╝  ██╔══██╗  ██╔══██║██║╚████║██║  ██║
          ╚██╔╝ ╚██╔╝ ██║  ██║██║ ╚███║██████╔╝███████╗██║  ██║  ██║  ██║██║ ╚███║██████╔╝
           ╚═╝   ╚═╝  ╚═╝  ╚═╝╚═╝  ╚══╝╚═════╝ ╚══════╝╚═╝  ╚═╝  ╚═╝  ╚═╝╚═╝  ╚══╝╚═════╝ 
        
         ██████╗██╗      █████╗ ██╗   ██╗ ██████╗ ██╗  ██╗████████╗███████╗██████╗
        ██╔════╝██║     ██╔══██╗██║   ██║██╔════╝ ██║  ██║╚══██╔══╝██╔════╝██╔══██╗
        ╚█████╗ ██║     ███████║██║   ██║██║  ██╗ ███████║   ██║   █████╗  ██████╔╝
         ╚═══██╗██║     ██╔══██║██║   ██║██║  ╚██╗██╔══██║   ██║   ██╔══╝  ██╔══██╗
        ██████╔╝███████╗██║  ██║╚██████╔╝╚██████╔╝██║  ██║   ██║   ███████╗██║  ██║
        ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                """
        return cover


if __name__ == "__main__":
    game = Game(shop, locations[0], locations, game_player)
    print(GameCover())
    current_location_map = "\n".join(locations[0].map)
    print(Map(current_location_map))
    while True:
        if game.defeated_bosses == 3:
            print(colored("Congratulations on completing the game!", "green", attrs=["bold"]))
            break
        print(game)
        print(game.run())
