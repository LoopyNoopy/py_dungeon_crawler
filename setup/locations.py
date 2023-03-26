from abc import ABC, abstractmethod
from setup import functions,weapons
import random
import keyboard
import os

clear = lambda: os.system('cls')

class baseLocation(ABC):

    def __init__(self, newLocationType):
        self.locationType = newLocationType
        self.locationName = functions.pickPlaceName(self.locationType)

class townClass(baseLocation):

    def __init__(self, player):
        super().__init__("town")
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

    def buyWeapon(self,firstWeapon = False):
        weaponNo = input("Please enter the number: ")
        if int(weaponNo) <= len(self.shopItems):
            return self.shopItems[int(weaponNo)]
        else:
            print("Naughty Number")
        return

    def cycleWeapons(self):
        userInput = None
        weaponNo = 0
        while userInput == None:
            print("Weapon number " + str(weaponNo))
            print(str(self.shopItems[weaponNo])+"\n")
            keyPress = keyboard.read_key()
            match keyPress:
                case "up":
                    weaponNo += 1
                    if weaponNo > len(self.shopItems) - 1:
                        weaponNo = 0
                    clear()

                case "down":
                    weaponNo -= 1
                    if weaponNo <= 0:
                        weaponNo = len(self.shopItems) -1
                    clear()
                case _:
                    # ToDo Fix accidental string keypress
                    if int(keyPress) <= len(self.shopItems) -1:
                        print("Key in range")
                    else:
                        print("Key not valid")
        return