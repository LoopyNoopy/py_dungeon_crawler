from abc import ABC, abstractmethod
import random

class baseWeapon(ABC):

    @abstractmethod
    def __init__(self, newLevel, newBaseAttack, newWeaponType):
        self.rarity = self.randomiseRarity()
        self.weaponLevel = newLevel
        self.attack = random.randint(newBaseAttack,newBaseAttack+5) * (self.weaponLevel*self.rarityModifier(self.rarity))
        self.weaponType = newWeaponType

    def randomiseRarity(self):
        rarityValue = random.randint(1,4)
        match rarityValue:
            case 1:
                return("Common")
            case 2:
                return("Rare")
            case 3:
                return("Epic")
            case 4:
                return("Legendary")

    def rarityModifier(self, rarity):
        match rarity:
            case "Common":
                return(1)
            case "Rare":
                return(1.25)
            case "Epic":
                return(1.5)
            case "Legendary":
                return(1.75)

    def getAttack(self):
        return(self.attack)

    def getWeaponType(self):
        return(self.weaponType)

    def printWeaponStats(self):
        print("Weapon Type: " + self.weaponType, "\nWeapon Level: " + str(self.weaponLevel), "\nWeapon Rarity: " + self.rarity, "\nWeapon Attack: " + str(self.attack))

class bowClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,10,"Bow")

class swordClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,15,"Sword")

class axeClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,20,"Axe")

class daggerClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,5,"Dagger")

class fistClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,1,"Fists")