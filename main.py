import random
from setup import characters, locations, functions

print("Welcome to Loopy Noopy's Dungeon Crawler!\n")
playerName = input("What is your characters name?\n")
player = characters.playerCharacter(playerName, 1)
newOrc = characters.orc(1)

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
# ToDO Make this use the cycle list function
playerWeapon = startingTown.cycleWeapons()
print(str(playerWeapon))
# ToDo Make a comment about weapons rarity
while player.health >= 1:
    print("In the loop")
    currentLocation = functions.randomiseEvent()
    if not currentLocation.getEnemyList() == None:
        enemiesAlive = True

        if len(currentLocation.getEnemyList()) == 1:
            print("An enemy has been spotted!")
        else:
            print("You engage " + str(len(currentLocation.getEnemyList())) + "enemies!")

        while enemiesAlive:
            functions.printBaseEnemyStats(currentLocation.getEnemyList())
            action = input("What do you want to do?\n1: Attack\n2: Heal\n3:Retreat\nChoice: ")
            match action:
                case "1":
                    print("Choose one to attack")
                    isEnemyDead = True
                    while isEnemyDead:
                        chosenEnemy = functions.cycleList(currentLocation.getEnemyList(), "Enemy")
                        if chosenEnemy.health < 0:
                            print("You shouldn't be beating a dead " + chosenEnemy.name +"\n Chose one that is alive.")
                        else:
                            isEnemyDead = False
                    print("Attacking "+str(chosenEnemy.name) + " for " + str(playerWeapon.attack))
                    chosenEnemy.health -= playerWeapon.attack
                    if chosenEnemy.health <= 0:
                        print("Enemy has been slain!")
                    else:
                        print("Enemy health is now " + str(chosenEnemy.health))
                case "2":
                    # ToDo Create a healing mechanic
                    print("nice try, you can't heal yet")

            #Check to see if all enemies are dead
            for enemy in currentLocation.getEnemyList():
                if enemy.health > 0:
                    enemiesAlive = True
                else:
                    enemiesAlive = False

    print(currentLocation.getEnemyList())
