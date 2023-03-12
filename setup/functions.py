from setup import weapons
import random

def pickWeapon(player):
    choiceMade = False
    while choiceMade == False:
        print("I am able to give you the following weapons to start your journey:\n 1: Bow", "2: Sword", "3: Axe",
              "4: Dagger", "5: Fists\n")
        weaponSelect = input("Tell me, what weapon do you want to start with?\n You can enter either the number, or name of your instrument of violence\n")
        weaponSelect = weaponSelect.capitalize()
        match weaponSelect:
            case "1":
                return(weapons.bowClass(player.level))
            case "Bow":
                return(weapons.bowClass(player.level))
            case "2":
                return(weapons.swordClass(player.level))
            case "Sword":
                return(weapons.swordClass(player.level))
            case "3":
                return(weapons.axeClass(player.level))
            case "Axe":
                return(weapons.axeClass(player.level))
            case "4":
                return(weapons.daggerClass(player.level))
            case "Dagger":
                return(weapons.daggerClass(player.level))
            case "5":
                return(weapons.fistClass(player.level))
            case "Fist":
                return(weapons.fistClass(player.level))
            case _:
                print("\nI'm sorry " + player.getName() + ", I do not understand your tounge. Please tell me the number or the name of the weapon in English")

def createTownList():
    with open("resources\\town_names.txt") as townFile:
        town_list = townFile.readlines()
    for count,town in enumerate(town_list):
        town_list[count] = town.rstrip("\n")
    return town_list

def pickTown(town = createTownList()):
    return town[random.randint(1,len(town) - 1)]