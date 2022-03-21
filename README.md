# walking_game
## Description
This game is so-called game-wanderer that allows the player to wander around, kill enemies and bosses, loot them and level up. The game itself is broken down in 6 modules each responsible with different aspect of the game. Those modules are:
- ```enemies.py``` which introduces Enemy, Boss and Battle class
- ```equipment.py``` which has Item, Weaponry, Weapon, Armour and Potion class
- ```generator.py``` which introduces Generator class with Item- and Map- generators
- ```locations_and_mapping.py``` which has the classes of Location and Map
- ```main.py``` which contains Game and GameFolder class
- ```player.py``` which introduce Player, Backpack and Shop class
## The gameplay
### Map and Locations
Map consists of 28 locations that player may visit. The most important locations are those with shop, marked with letter ```S``` and those, which are marked with ```B```, the boss locations. Shop locations are important, because you may sell items you won in fights and buy useful potions that boost your damage and defense for the whole fight! And the completion of Boss locations are important, because after defeating 3 Bosses the game is finished. In order to know the name of the location and other info type ```location``` command, if you are interested only with map, than type ```map``` and if you decide to move between locations use the ```move``` command and afterwards choose the direction (```west```, ```north```, ```east``` or ```south```) to move to.
### Fight
In order to begin a fight on location, type the command ```fight``` and fight will begin. In the fight player may damage the enemy with weapon (```damage``` command) or use the potions bought in the shop in order to boost your damage, protection or health (```backpack``` command). To finish choosing potions type ```finish```. in the fight the most important parameters are ```damage```, ```protection``` and ```health```. In the fight protection allows you to decrease the damage done by enemy for it's numeric amount. The same system works for enemies. That's why it is crucially important to equip weapon or armour before fight (```equip``` command). You can also take off those pieces of equipment with ```unequip``` command. For every won fight you will be granted with points. If there is more than 20 points you level up and your points value return to 0. Maximum per fight you may gain 3 points, 1 point is minimum. In order to know the full stistic of yourself be sure to type ```me``` command. It will show you all your parameters including weapons equipped. Of course, after battle mobs will drop loot which will be automatically added to your backpack. In order to know what loot you have achieved after the fight be sure to type ```backpack``` command.
### Shopping
Shopping is available only at the locations marked with ```S```. If you are on the one of such locations than commands ```sell``` and ```buy``` will appear on your actions menu. Loot gained in fight may be sold in shops for the price mentioned in that description. You also may buy 3 possible potions which are:
- bear potion
- porcupine potion
- heal potion

Their descriptions may be found in the shop menu. In order to finish shopping type ```finish```
# Enjoy the game!
