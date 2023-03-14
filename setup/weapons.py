from abc import ABC, abstractmethod
import random

class baseWeapon(ABC):

    @abstractmethod
    def __init__(self, newLevel, newBaseAttack, newWeaponType):
        self.rarity = self.randomiseRarity()
        self.weaponLevel = newLevel
        self.attack = random.randint(newBaseAttack,newBaseAttack+5) * (self.weaponLevel*self.rarityModifier(self.rarity))
        self.weaponType = newWeaponType
        #ToDo Scale value with level, attack and rarity
        self.value = 100

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

    @abstractmethod
    def __str__(self):
        return f'Weapon type: {self.weaponType} \nWeapon level: {self.weaponLevel} \nWeapon rarity: {self.rarity} \nWeapon attack: {self.attack}'

class bowClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,10,"Bow")

    def __str__(self):
        return super().__str__()

class swordClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,15,"Sword")

    def __str__(self):
        return super().__str__()

class axeClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,20,"Axe")

    def __str__(self):
        return super().__str__()

class daggerClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,5,"Dagger")

    def __str__(self):
        return super().__str__()

class fistClass(baseWeapon):
    def __init__(self, newLevel):
        super().__init__(newLevel,1,"Fists")

    def __str__(self):
        return super().__str__()