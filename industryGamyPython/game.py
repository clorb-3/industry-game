import time
import os
import random
import json


def textScroll(inputString,
               delay=0.01):

    # this will be used to print text in a way that looks better than
    # just a print() function

    for letter in inputString:
        print(letter, end='', flush=True)
        time.sleep(delay)

    print()


def screenReset(printMaterials=True):

    # this clears the screen and prints user materials

    os.system('cls' if os.name == 'nt' else 'clear')

    global playerChar
    output = ''

    if printMaterials is True:
        for letter in str(playerChar['materials']):
            if letter in ["'", "{", "}"]:
                output = output

            else:
                output = output + letter

        print(output)


def userPrompting(questionText,
                  promptType="YesNo",
                  customPrompt="None",
                  customChoices="None",
                  requiedMatchingChoice=True):

    # prompt types will change the text displayed to the player
    # and the data types returned to the game

    while True:
        if not (questionText == ''):
            textScroll(questionText)

        if promptType == "custom":
            textScroll(customPrompt)
            choice = input(":> ").strip().lower()

            if (choice in customChoices) or (requiedMatchingChoice is False):
                return (choice)
                os.system('cls' if os.name == 'nt' else 'clear')

            textScroll("Invalid choice")
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif promptType == "YesNo":
            textScroll("[Y]es, [n]o")
            return (False if ("n" or "N") in input(":> ") else True)

        elif promptType == "NoYes":
            textScroll("[y]es, [N]o")
            return (True if ("y" or "Y") in input(":> ") else False)


def charicterCreation():

    screenReset(False)
    textScroll("hello, welcome to the first bata version" +
               " of a game I'm concepting")
    time.sleep(3)
    screenReset(False)

    global playerChar
    playerChar = {'isUser': True, 'hasFailed': False}
    playerChar['name'] = userPrompting("",
                                       "custom",
                                       "Charicter name",
                                       "None",
                                       False)
    setStartMaterials()

    global saveData
    saveData['chars'] = {}
    saveData['chars']['playerChar'] = playerChar

    return ()


def setStartMaterials():

    global playerChar

    playerChar['materials'] = {}
    playerChar['materials']['iron'] = random.randint(50, 75)
    playerChar['materials']['rawWood'] = random.randint(50, 75)

    return ()


def doTurns():
    global playerChar
    hoursInDay = 24
    while hoursInDay > 0:

        return ()


def checkForPlayerFailure():

    return ()


def runPlayerFail():

    screenReset()
    textScroll(str(playerChar['name']) + " has gone bankrupt")
    print()

    return ()


def saveGame():

    global saveData
    global playerChar

    saveData['chars']['playerChar'] = playerChar

    with open('saveData.json', 'w') as file:
        json.dump(saveData, file, indent=2)

    return ()


def loadGame():

    global saveData
    global playerChar

    with open('saveData.json', 'r') as file:
        saveData = json.load(file)

    playerChar = saveData['chars']['playerChar']

    return ()


def startGameInstance():

    try:
        loadGame()
    except FileNotFoundError:
        with open('saveData.json', 'w') as file:
            json.dump({}, file)

    try:
        if playerChar['hasFailed'] is True:
            charicterCreation()
            saveGame()
    except KeyError:
        charicterCreation()
        saveGame()

    global gameData
    with open('gameData.json', 'r') as file:
        gameData = json.load(file)

    return ()


def main():

    startGameInstance()

    while playerChar['hasFailed'] is False:
        doTurns()
        checkForPlayerFailure()

    runPlayerFail()


saveData = {}
gameData = {}
playerChar = {}

if __name__ == "__main__":
    main()
