from setup import characters, weapons, functions

print("Welcome to Loopy Noopys Dungeon Crawler!\n")
playerName = input("What is your characters name?\n")
player = characters.playerCharacter(playerName,1)
print("Welcome " + player.getName()+"!")
playerWeapon = functions.pickWeapon(player)
playerWeapon.printWeaponStats()
