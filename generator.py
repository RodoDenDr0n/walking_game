import json
from equipment import Weapon, Armour, Weaponry, Potion
from route import Location
from random import shuffle


class Generator:
    def __init__(self, data=None, generated=None):
        self.data = data
        self.generated = generated

    def generate_container(self):
        pass

    def read_file(self, file):
        with open(file, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        self.data = data

    def divide_by_purpose(self):
        pass

    def generate_objects(self, file):
        self.generate_container()
        self.read_file(file)
        self.divide_by_purpose()


class ItemGenerator(Generator):
    def generate_container(self):
        leveled_equipment = {}
        for i in range(1, 9):
            leveled_equipment.setdefault(i, [])
        leveled_equipment.setdefault("potions", [])
        self.generated = leveled_equipment

    def read_file(self, file):
        super().read_file(file)

    def divide_by_purpose(self):
        for value in self.data.values():
            for name, characteristics in value.items():
                characteristics = tuple(characteristics.values())
                if len(characteristics) == 3:
                    damage, protection, price = characteristics
                    if damage != 0:
                        item = Weapon(name, damage, price)
                    else:
                        item = Armour(name, protection, price)
                else:
                    description, price = characteristics
                    item = Potion(name, description, price)

                if isinstance(item, Weaponry):
                    if item.damage in range(1, 3) or item.protection in range(1, 2):
                        self.generated[1].append(item)
                    if item.damage in range(2, 4) or item.protection in range(1, 3):
                        self.generated[2].append(item)
                    if item.damage in range(3, 5) or item.protection in range(2, 4):
                        self.generated[3].append(item)
                    if item.damage in range(3, 6) or item.protection in range(3, 5):
                        self.generated[4].append(item)
                    if item.damage in range(4, 7) or item.protection in range(3, 6):
                        self.generated[5].append(item)
                    if item.damage in range(5, 8) or item.protection in range(4, 6):
                        self.generated[6].append(item)
                    if item.damage in range(6, 9) or item.protection in range(5, 7):
                        self.generated[7].append(item)
                    if item.damage in range(7, 11) or item.protection in range(5, 9):
                        self.generated[8].append(item)
                else:
                    self.generated["potions"].append(item)

    def generate_objects(self, file):
        super().generate_objects(file)


class MapGenerator(Generator):
    def generate_container(self):
        self.generated = []

    def read_file(self, file):
        super().read_file(file)

    def divide_by_purpose(self):
        streets_list = ["Ivana-Franka Street", "Voloska Street", "Zelena Street", "Paliya Street",
                        "Kostia Levytskoho Street", "Kl'onovycha Street", "Akademika Bohomol'tsya Street",
                        "Volodymyra Vynnychenka Street", "Maksyma Kryvonosa Street", "Ivana Gonty Street",
                        "Krakivska Street", "The Lviv Theatre of Opera and Ballet", "Town Hall", "Potocki Palace",
                        "Armenian Quarter", "Lychakiv Cemetry", "Italian Courtyard", "Dormition Cathedral",
                        "Lviv National Ivan Franko University", "Pharmacy Museum", "Lviv Arsenal",
                        "Library of Ukrainian Catholic University", "Pidvalna Street", "Stavropihiiska Street",
                        "Rynok Square", "Virmenska Street", "Mykoly Kopernyka Street", "Svobody Ave"]
        shuffle(streets_list)
        for key, value in self.data.items():
            self.generated.append(Location(streets_list[int(key)], int(key), value[0], False, False, value[1]))

    def generate_objects(self, file):
        super().generate_objects(file)
