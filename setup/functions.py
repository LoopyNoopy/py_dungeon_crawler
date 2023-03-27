from setup import weapons, locations
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

def weaponMaker(player):
    weaponSelecter  = random.randint(1,5)
    match weaponSelecter:
        case 1:
            return (weapons.bowClass(player.level))
        case 2:
            return (weapons.swordClass(player.level))
        case 3:
            return (weapons.axeClass(player.level))
        case 4:
            return (weapons.daggerClass(player.level))
        case 5:
            return (weapons.fistClass(player.level))
def createPlaceList(type):
    with open("resources\\{0}_names.txt".format(type)) as textFile:
        nameList = textFile.readlines()
    for count,town in enumerate(nameList):
        nameList[count] = town.rstrip("\n")
    return nameList

def pickPlaceName(type):
    nameList = createPlaceList(type)
    return nameList[random.randint(1,len(nameList) - 1)]

def randomiseEvent():
    location = locations.fieldClass
    return location