from abc import ABC, abstractmethod

class baseCharacter(ABC):
    @abstractmethod
    def __init__(self, newName, newLevel):
        self.name = newName
        self.level = newLevel
        if self.level == 1:
            self.exp, self.health, self.attack = 100, 100, 100
        else:
            #TODO Make these scale by level
            self.exp, self.health, self.attack = 100, 100, 100
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
