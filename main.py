from setup import characters, weapons, functions

print("Welcome to Loopy Noopys Dungeon Crawler!\n")
playerName = input("What is your characters name?\n")
player = characters.playerCharacter(playerName,1)
startingTown = functions.pickTown()
print("Welcome to " + startingTown + ", " + player.getName()+"!")
playerWeapon = functions.pickWeapon(player)
print(str(playerWeapon))
##ToDo Make a comment about weapons rarity

