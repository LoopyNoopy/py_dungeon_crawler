from setup import weapons, locations
import random, keyboard, os

def clearConsole():
    clear = lambda: os.system('cls')
    return clear

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
    location = locations.fieldClass()
    return location

def getPlayerLevelFromFile():
    with open("resources\gameVariables.txt","r") as file:
        fileLines = file.readlines()
        return fileLines[0].rstrip("\n")

def cycleList(theList):
    itemNo = 0
    while True:
        print("Weapon number: " + str(itemNo))
        print(str(theList[itemNo]) + "\n")
        keyPress = keyboard.read_key()
        match keyPress:
            case "up":
                itemNo += 1
                if itemNo > len(theList) - 1:
                    itemNo = 0
                clearConsole()

            case "down":
                itemNo -= 1
                if itemNo <= 0:
                    itemNo = len(theList) - 1
                clearConsole()
            case _:
                # ToDo Fix duplicate string keypress
                if keyPress.isnumeric():
                    if int(keyPress) <= len(theList) - 1:
                        print("\nList number: " + str(keyPress))
                        print(str(theList[int(keyPress)]))
                        finalChoice = input(
                            "\nAre you sure you want to select " + str(keyPress) + "?\ny for yes, n for no: ")
                        match finalChoice:
                            case "y":
                                # ToDo something about choice
                                return theList[int(keyPress)]
                            case "n":
                                print("Please make your selection...\n")
                else:
                    # ToDo Randomise these comments
                    print("\nYou can't pick the ground, try again.")
    return