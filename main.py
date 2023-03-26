from setup import characters, locations

print("Welcome to Loopy Noopy's Dungeon Crawler!\n")
playerName = input("What is your characters name?\n")
player = characters.playerCharacter(playerName, 1)
startingTown = locations.townClass(player)
startingTown.cycleWeapons()
# ToDo Use language file
print("Welcome to " + str(startingTown) + ", " + player.getName() + "!\nSeeing as you don't have anything to defend "
                                                                    "yourself with I can see you're new here... How you"
                                                                    "managed to survive out there I don't know.\nCome "
                                                                    "with me to the towns shop and let me get you a "
                                                                    "weapon. The shopkeeper owes me a favour, "
                                                                    "and now you will owe me one!\n\nAh hello! Please "
                                                                    "take a look and tell me what you like!")
startingTown.printShopItems()
playerWeapon = startingTown.buyWeapon()
# ToDo Make this list scrollable with arrow keys
print(str(playerWeapon))
# ToDo Make a comment about weapons rarity
while player.health >= 1:
    # ToDo create new scenario
    # ToDo act in scenario
    print("In the loop")
    print(str(player.health))
    player.health = 0