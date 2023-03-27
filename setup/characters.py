import random
from abc import ABC, abstractmethod
from setup import weapons

class baseCharacter(ABC):
    @abstractmethod
    def __init__(self, newName, newLevel):
        self.name = newName
        self.level = newLevel
        if self.level == 1:
            self.exp, self.health, self.coin = 0, 100, 100
        else:
            #TODO Make these scale by level
            self.exp, self.health, self.coin = 100, 100, 100
        self.nextLevelExp = self.exp * 1.15
        return

    def newLevelGained(self):
        self.level += 1
        self.nextLevelExp

    def getName(self):
        return(self.name)

class playerCharacter(baseCharacter):
    def __init__(self, newName, newLevel):
        super().__init__(newName, newLevel)

class orc(baseCharacter):
    def __init__(self, levelModifier):
        orcLevel = random.randint(levelModifier-1, levelModifier+1)
        if orcLevel <= 0:
            orcLevel = 1
        super().__init__("Orc",orcLevel)
        self.weapon = weapons.axeClass(orcLevel)

    def __str__(self):
        return f'Enemy type: {self.name} \nEnemy level: {self.level} \n{str(self.weapon)}\n'