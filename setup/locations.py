from abc import ABC, abstractmethod
from setup import functions,weapons,characters
import random
import keyboard
import os

class baseLocation(ABC):

    def __init__(self, newLocationType, enemiesPossible):
        self.locationType = newLocationType
        self.locationName = functions.pickPlaceName(self.locationType)
        if enemiesPossible:
            self.enemiesPresent = True
            if self.randomsieCombat():
                enemyClasses = characters.enemy.__subclasses__()
                self.enemies = [None] * random.randint(1,3)
                for enemy in range(len(self.enemies)):
                    self.enemies[enemy] = enemyClasses[random.randint(0,len(enemyClasses)-1)](int(functions.getPlayerLevelFromFile()))
                return
            else:
                self.enemiesPresent = False

    def randomsieCombat(self):
        if random.randint(0,1) == 1:
            return True
        else:
            return False
    def getEnemyList(self):
        if self.enemiesPresent == True:
            return self.enemies
        else:
            return None
class townClass(baseLocation):

    def __init__(self, player):
        super().__init__("town", False)
        self.shopItems = []
        for item in range(random.randint(3, 7)):
            self.shopItems.append(functions.weaponMaker(player))

    def __str__(self):
        return self.locationName

    def printShopItems(self):
        # ToDo "Weapon 0" doesn't exist
        for item in range(len(self.shopItems)):
            print("Weapon number " + str(item))
            print(str(self.shopItems[item])+"\n")
        return

    def buyWeapon(self,weaponNo,firstWeapon = False):
        if int(weaponNo) <= len(self.shopItems):
            return self.shopItems[int(weaponNo)]
        else:
            print("Naughty Number")
        return

    def cycleWeapons(self):
        # Todo make use of the cycle weapons in functions.py
        userInput = None
        weaponNo = 0
        while userInput == None:
            print("Weapon number: " + str(weaponNo))
            print(str(self.shopItems[weaponNo])+"\n")
            keyPress = keyboard.read_key()
            match keyPress:
                case "up":
                    weaponNo += 1
                    if weaponNo > len(self.shopItems) - 1:
                        weaponNo = 0
                    functions.clear

                case "down":
                    weaponNo -= 1
                    if weaponNo <= 0:
                        weaponNo = len(self.shopItems) -1
                    functions.clear
                case _:
                    # ToDo Fix duplicate string keypress
                    if keyPress.isnumeric():
                        if int(keyPress) <= len(self.shopItems) -1:
                            print("\nWeapon number: "+str(keyPress))
                            print(str(self.shopItems[int(keyPress)]))
                            finalChoice = input("\nAre you sure you want to select weapon "+str(keyPress)+"?\ny for yes, n for no: ")
                            match finalChoice:
                                case "y":
                                    return self.buyWeapon(int(keyPress))
                                case "n":
                                    print("Putting weapon back on the shelf...\n")
                    else:
                        # ToDo Randomise these comments
                        print("\nI don't speak orc child, use your words.")
        return

class fieldClass(baseLocation):
    def __init__(self):
        super().__init__("field",True)
