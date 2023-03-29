import random
from setup import characters, locations, functions

print("Welcome to Loopy Noopy's Dungeon Crawler!\n")
playerName = input("What is your characters name?\n")
player = characters.playerCharacter(playerName, 1)
with open("resources\gameVariables.txt", "w+") as liveFile:
    liveFile.write(str(player.level))
startingTown = locations.townClass(player)
print("Welcome to " + str(startingTown) + ", " + player.getName() + "!\nSeeing as you don't have anything to defend "
                                                                    "yourself with I can see you're new here... How you"
                                                                    "managed to survive out there I don't know.\nCome "
                                                                    "with me to the towns shop and let me get you a "
                                                                    "weapon. The shopkeeper owes me a favour, "
                                                                    "and now you will owe me one!\n\nAh hello! Please "
                                                                    "take a look and tell me what you like!")
#startingTown.printShopItems()
playerWeapon = startingTown.cycleWeapons()
# ToDo Make this list scrollable with arrow keys
print(str(playerWeapon))
# ToDo Make a comment about weapons rarity
while player.health >= 1:
    print("In the loop")
    currentLocation = functions.randomiseEvent()
    if not currentLocation.getEnemyList() == None:
        enemiesAlive = True
        while enemiesAlive == True:
            for enemy in currentLocation.enemies:
                if enemy.health >=0:
                    enemiesAlive = False
                else:
                    enemiesAlive = True


    print(currentLocation.getEnemyList())
