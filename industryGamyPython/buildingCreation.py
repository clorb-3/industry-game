import json
import os


def clearTerm():

    os.system('cls' if os.name == 'nt' else 'clear')

    return ()


def initalize():

    global buildingData
    with open('gameData.json', 'r') as file:
        buildingData = json.load(file)
    buildingData = buildingData['buildingData']

    return ()


def saveData():

    with open('gameData.json', 'r') as file:
        gameData = json.load(file)

    gameData['buildingData'] = buildingData

    with open('gameData.json', 'w') as file:
        json.dump(gameData, file, indent=2)


def printJson(data):

    print(json.dumps(data, indent=2))

    return ()


def editingRecursive(editObj, recTimes=0):

    recTimes = recTimes + 1

    while True:
        clearTerm()
        printJson(editObj)

        whatToEdit = input('what to edit\n:> ').strip().capitalize()
        try:
            if whatToEdit == 'Done':

                return (editObj)

            elif whatToEdit == 'Name' and recTimes == 1:

                global buildingData

                newName = input('new name\n:> ').strip().capitalize()
                oldName = editObj['Name']
                if newName == oldName:
                    return (editObj)

                if newName == 'Delete':
                    del buildingData[oldName]
                    return ('Deleted structure')

                buildingData[oldName]['Name'] = newName
                buildingData[newName] = buildingData[oldName]
                del buildingData[oldName]

                return ({'Renamed structure to': newName})

            elif str(type(editObj[whatToEdit])) == "<class 'dict'>":

                editObj[whatToEdit] = editingRecursive(editObj[whatToEdit],
                                                       recTimes)

            else:

                editObj[whatToEdit] = input('new value \n:> ')

        except KeyError:
            print(whatToEdit + " is not a stat.\ndo you want to add a new stat"
                  + "?\nkeep in mind that assigned stats will likely not hav" +
                  "e a use.")
            try:
                if (input("[y]es or [N]o\n:> ").lower())[0] == 'y':
                    editObj[whatToEdit] = input('value of new stat: ' +
                                                whatToEdit + '\n:> '
                                                ).strip().capitalize()

            except IndexError:
                pass


def makeNewStructure(name):

    global buildingData
    buildingData[name] = {"Name": name,
                          "Price": {},
                          "Passive": {},
                          "Active": {}}

    pass


def programRunTime():

    clearTerm()

    global buildingData
    for i in buildingData:
        try:
            print(buildingData[i]['Name'])

        except KeyError:
            print(i + ' ' + str(buildingData[i]))

    selection = input(':> ').strip().capitalize()
    try:
        if selection == 'Done':
            return (False)

        else:
            buildingData[selection] = editingRecursive(buildingData[selection])

    except KeyError:

        print(selection + " is not a building would you like to make it one?")
        try:
            if (input("[y]es [N]o\n:> ").strip().lower())[0] == 'y':
                makeNewStructure(selection)

        except IndexError:
            pass

    return (True)


def main():
    initalize()
    while programRunTime():
        pass
    printJson(buildingData)
    saveData()


if __name__ == "__main__":
    main()
