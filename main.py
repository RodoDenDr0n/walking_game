from player import Player, Backpack, Shop
from generator import ItemGenerator, MapGenerator
from termcolor import colored
from route import Compass, Map
from enemies import Enemy, Battle
from equipment import Weaponry, Weapon, Armour

backpack = Backpack()
game_player = Player(backpack)

item_generator = ItemGenerator()
item_generator.generate_objects("items.json")  # generates dictionary with key:level, value:items list
map = MapGenerator()
map.generate_objects("map.json")  # generates list of locations
locations = map.generated

shop = Shop(backpack, game_player, item_generator.generated["potions"])

# test_weapon = Weaponry("weapon", 5, 0, 10)
# test_potion = Potion("potion", "potion created for testing", 10)
# backpack.add_item(test_weapon)
# backpack.add_item(test_weapon)
# backpack.add_item(test_potion)
class Game:
    def __init__(self, shop, current_location, locations, game_player):
        self.item_generator = item_generator
        self.shop = shop
        self.current_location = current_location
        self.locations = locations
        self.game_player = game_player

    def proceed_commands(self):
        pass

    def main(self):
        command = input("\nEnter the " + colored("command", "green") + ":" +
                        colored("\n>>> ", "red", attrs=["bold"]))

        if command == "sell":
            return self.shop.sell()

        elif command == "buy":
            return self.shop.buy()

        elif command == "backpack":
            return str(self.game_player.backpack)

        elif command == "me":
            return str(self.game_player)

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
                    return f"You moved {direction}"
            return colored(f"You can't go {direction}", "red", attrs=["bold"])

        elif command == "map":
            current_location_map = "\n".join(self.current_location.map)
            return Map(current_location_map)

        elif command == "fight":
            enemy = Enemy.spawn(game_player.level)
            result = Battle(game_player, enemy).fight()
            if result:
                game_player.set_default_stats()
                level_items = item_generator.generated[game_player.level]
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
            for element in self.game_player.backpack.equipment:
                if isinstance(element, equipment_type):
                    message += str(element)
            print(message)

            chosen_equipment = input(colored("Equip: ", "red", attrs=["bold"]))
            if equipment_type == Weapon:
                game_player.equip_weapon(chosen_equipment)
            elif equipment_type == Armour:
                game_player.equip_armour(chosen_equipment)

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


game = Game(shop, locations[0], locations, game_player)
while True:
    print(game.main())
