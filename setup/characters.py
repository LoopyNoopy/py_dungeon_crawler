class base_character():
    def __int__(self, newName, newLevel) -> object:
        name = newName
        level = newLevel
        if level == 1:
            exp, health, attack = 100
        else:
            exp, health, attack = 100 * 1.15
        nextLevelExp = exp * 1.15

    def newLevelGained(self):
        self.level += 1
        self.nextLevelExp
