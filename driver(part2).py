from pyswip import *
import random

rows = 6
cols = 7

rrows = (rows*2) - 1
rcols = (cols*2) -1
rMapCell = [".", ".", ".", " ", "?", " ", ".", ".", "."]

mapCell = [".", ".", ".", " ", "?", " ", ".", ".", "."]
wall = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
map = []
map = []

actionSequence = []

dictionary = {
    (1, 4): 8,
    (2, 4): 9,
    (3, 4): 10,
    (4, 4): 11,
    (5, 4): 12,
    (1, 3): 15,
    (2, 3): 16,
    (3, 3): 17,
    (4, 3): 18,
    (5, 3): 19,
    (1, 2): 22,
    (2, 2): 23,
    (3, 2): 24,
    (4, 2): 25,
    (5, 2): 26,
    (1, 1): 29,
    (2, 1): 30,
    (3, 1): 31,
    (4, 1): 32,
    (5, 1): 33
}

rdictionary = {
    (0,10): 0,
    (1,10): 1,
    (2,10): 2,
    (3,10): 3,
    (4,10): 4,
    (5,10): 5,
    (6,10): 6,
    (7,10): 7,
    (8,10): 8,
    (9,10): 9,
    (10,10): 10,
    (11,10): 11,
    (12,10): 12,
    (0,9): 13,
    (1,9): 14,
    (2,9): 15,
    (3,9): 16,
    (4,9): 17,
    (5,9): 18,
    (6,9): 19,
    (7,9): 20,
    (8,9): 21,
    (9,9): 22,
    (10,9): 23,
    (11,9): 24,
    (12,9): 25,
    (0,8): 26,
    (1,8): 27,
    (2,8): 28,
    (3,8): 29,
    (4,8): 30,
    (5,8): 31,
    (6,8): 32,
    (7,8): 33,
    (8,8): 34,
    (9,8): 35,
    (10,8): 36,
    (11,8): 37,
    (12,8): 38,
    (0,7): 39,
    (1,7): 40,
    (2,7): 41,
    (3,7): 42,
    (4,7): 43,
    (5,7): 44,
    (6,7): 45,
    (7,7): 46,
    (8,7): 47,
    (9,7): 48,
    (10,7): 49,
    (11,7): 50,
    (12,7): 51,
    (0,6): 52,
    (1,6): 53,
    (2,6): 54,
    (3,6): 55,
    (4,6): 56,
    (5,6): 57,
    (6,6): 58,
    (7,6): 59,
    (8,6): 60,
    (9,6): 61,
    (10,6): 62,
    (11,6): 63,
    (12,6): 64,
    (0,5): 65,
    (1,5): 66,
    (2,5): 67,
    (3,5): 68,
    (4,5): 69,
    (5,5): 70,
    (6,5): 71,
    (7,5): 72,
    (8,5): 73,
    (9,5): 74,
    (10,5): 75,
    (11,5): 76,
    (12,5): 77,
    (0,4): 78,
    (1,4): 79,
    (2,4): 80,
    (3,4): 81,
    (4,4): 82,
    (5,4): 83,
    (6,4): 84,
    (7,4): 85,
    (8,4): 86,
    (9,4): 87,
    (10,4): 88,
    (11,4): 89,
    (12,4): 90,
    (0,3): 91,
    (1,3): 92,
    (2,3): 93,
    (3,3): 94,
    (4,3): 95,
    (5,3): 96,
    (6,3): 97,
    (7,3): 98,
    (8,3): 99,
    (9,3): 100,
    (10,3): 101,
    (11,3): 102,
    (12,3): 103,
    (0,2): 104,
    (1,2): 105,
    (2,2): 106,
    (3,2): 107,
    (4,2): 108,
    (5,2): 109,
    (6,2): 110,
    (7,2): 111,
    (8,2): 112,
    (9,2): 113,
    (10,2): 114,
    (11,2): 115,
    (12,2): 116,
    (0,1): 117,
    (1,1): 118,
    (2,1): 119,
    (3,1): 120,
    (4,1): 121,
    (5,1): 122,
    (6,1): 123,
    (7,1): 124,
    (8,1): 125,
    (9,1): 126,
    (10,1): 127,
    (11,1): 128,
    (12,1): 129,
    (0,0): 130,
    (1,0): 131,
    (2,0): 132,
    (3,0): 133,
    (4,0): 134,
    (5,0): 135,
    (6,0): 136,
    (7,0): 137,
    (8,0): 138,
    (9,0): 139,
    (10,0): 140,
    (11,0): 141,
    (12,0): 142
}

def get_key(val):
    for key, value in dictionary.items():
         if val == value:
             return key
 
    return "key doesn't exist"

xOffset = 6
yOffset = 5

# agent's position
agentPos = {
    
    
}


# update agent's position
def updateAgent(x, y, dir):
    agentPos["x"] = x
    agentPos["y"] = y
    agentPos["dir"] = dir

# reset agent
def resetAgent():
    agentPos.clear()

# Build Percept List
# Confounded, Stench, Tingle, Glitter, Bump, Scream
# 0, 1, 2, 6, 7, 8
def getPercepts(List):
    L = []

    # Confounded
    if List[0] != ".":
        L.append("on")
    else:
        L.append("off")

    # Stench
    if List[1] != ".":
        L.append("on")
    else:
        L.append("off")
    
    # Tingle
    if List[2] != ".":
        L.append("on")
    else:
        L.append("off")

    # Glitter
    if List[6] != ".":
        L.append("on")
    else:
        L.append("off")

    # Bump
    if List[7] != ".":
        L.append("on")
    else:
        L.append("off")

    # Scream
    if List[8] != ".":
        L.append("on")
    else:
        L.append("off")

    return L

def createMap(mapType):
    if mapType == "absolute":
        absoluteMap = []
        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    absoluteMap.append(wall.copy())
                elif i == rows - 1:
                    absoluteMap.append(wall.copy())
                elif 0 < i < rows - 1:
                    if j == 0:
                        absoluteMap.append(wall.copy())
                    elif j == cols - 1:
                        absoluteMap.append(wall.copy())
                    else:
                        absoluteMap.append(mapCell.copy())
        for cells in absoluteMap:
            if cells[4] != "W" or cells[4] != "O":
                cells[4] = "s"
        return absoluteMap
    elif mapType == "relative":
        relativeMap = []
        for i in range(rrows):
            for j in range(rcols):
                relativeMap.append(rMapCell.copy())
        return relativeMap

def printMap(mapType,map):
    if mapType=="absolute":
        print("============================================================")
        print("========================ABSOLUTE MAP========================")
        print()
        current = cols
        prev = 0
        total = rows * cols
        while total > 0:
            for i in range(prev, current, 1):
                for j in range(0, 3, 1):
                    print(map[i][j], end=" ")
                print(" ", end=" ")
            print()
            for i in range(prev, current, 1):
                for j in range(3, 6, 1):
                    print(map[i][j], end=" ")
                print(" ", end=" ")
            print()
            for i in range(prev, current, 1):
                for j in range(6, 9, 1):
                    print(map[i][j], end=" ")
                print(" ", end=" ")

            print()
            print()

            prev = current
            current = current + cols
            total = total - cols
        print("============================================================")

    elif mapType=="relative":
        print("============================================================")
        print("========================RELATIVE MAP========================")
        print()
        print(actionSequence)
        current = rcols
        prev = 0
        total = rrows * rcols
        while total > 0:
            for i in range(prev, current, 1):
                for j in range(0, 3, 1):
                    print(map[i][j], end=" ")
                print(" ", end=" ")
            print()
            for i in range(prev, current, 1):
                for j in range(3, 6, 1):
                    print(map[i][j], end=" ")
                print(" ", end=" ")
            print()
            for i in range(prev, current, 1):
                for j in range(6, 9, 1):
                    print(map[i][j], end=" ")
                print(" ", end=" ")

            print()
            print()

            prev = current
            current = current + rcols
            total = total - rcols
        print("============================================================")

def stenchOn(x, y,absoluteMap):
    absoluteMap[dictionary[(x, y)]][1] = "="


def tingleOn(x, y,absoluteMap):
    absoluteMap[dictionary[(x, y)]][2] = "T"


def npcOn(x, y, absoluteMap):
    absoluteMap[dictionary[(x, y)]][3] = "-"
    absoluteMap[dictionary[(x, y)]][5] = "-"


def wumpusOn(x, y,absoluteMap):
    print("Placing Wumpus at: (", x, ",", y, ")")
    index = dictionary.get((x, y))

    absoluteMap[index][4] = "W"

    # Set Stench indicator up, down, left and right around Wumpus

    # up
    index = dictionary.get((x, y + 1))

    if index:
        print("Stench indicator on at: (", x, ",", y + 1, ")")
        if absoluteMap[index][1] != "#":
            absoluteMap[index][1] = "="
    
    # down
    index = dictionary.get((x, y - 1))

    if index:
        print("Stench indicator on at: (", x, ",", y - 1, ")")
        if absoluteMap[index][1] != "#":
            absoluteMap[index][1] = "="
    # left
    index = dictionary.get((x - 1, y))

    if index:
        print("Stench indicator on at: (", x - 1, ",", y, ")")
        if absoluteMap[index][1] != "#":
            absoluteMap[index][1] = "="
    # right
    index = dictionary.get((x + 1, y))

    if index:
        print("Stench indicator on at: (", x + 1, ",", y, ")")
        if absoluteMap[index][1] != "#":
            absoluteMap[index][1] = "="


def portalOn(x, y,absoluteMap):
    print("Placing Portal at: (", x, ",", y, ")")
    absoluteMap[dictionary[(x, y)]][4] = "O"

    # Set Tingle indicator up, down, left and right around Portal
    # up
    index = dictionary.get((x, y + 1))

    if index:
        print("Tingle indicator on at: (", x, ",", y + 1, ")")
        if absoluteMap[index][2] != "#":
            absoluteMap[index][2] = "T"
    # down
    index = dictionary.get((x, y - 1))

    if index:
        print("Tingle indicator on at: (", x, ",", y - 1, ")")
        if absoluteMap[index][2] != "#":
            absoluteMap[index][2] = "T"
    # left
    index = dictionary.get((x - 1, y))
    if index:
        print("Tingle indicator on at: (", x - 1, ",", y, ")")
        if absoluteMap[index][2] != "#":
            absoluteMap[index][2] = "T"
    # right
    index = dictionary.get((x + 1, y))
    if index:
        print("Tingle indicator on at: (", x + 1, ",", y, ")")
        if absoluteMap[index][2] != "#":
            absoluteMap[index][2] = "T"

def coinOn(x, y,absoluteMap):
    print("Placing Coin at: (", x, ",", y, ")")
    absoluteMap[dictionary[(x, y)]][4] = "?"

    # Set Glitter indicator
    absoluteMap[dictionary[(x, y)]][6] = "*"

def agentOn(x, y, dir,absoluteMap):
    print("Placing Agent at: (", x, ",", y, ")", dir)
    if dir == "North":
        absoluteMap[dictionary[(x, y)]][4] = "^"
    elif dir == "South":
        absoluteMap[dictionary[(x, y)]][4] = "v"
    elif dir == "East":
        absoluteMap[dictionary[(x, y)]][4] = ">"
    elif dir == "West":
        absoluteMap[dictionary[(x, y)]][4] = "<"

    # Set Agent indicator
    absoluteMap[dictionary[(x, y)]][3] = "-"
    absoluteMap[dictionary[(x, y)]][5] = "-"
    agentPos["x"] = x
    agentPos["y"] = y
    agentPos["dir"] = dir

def initialize():
    absoluteMap = createMap("absolute")
    print("Initializing Empty Map...")

    wumpusOn(1, 3,absoluteMap)
    portalOn(5, 4,absoluteMap)
    portalOn(4, 3,absoluteMap)
    portalOn(4, 1,absoluteMap)
    coinOn(2, 3,absoluteMap)
    coinOn(1, 2, absoluteMap)
    #agentOn(1, 1, "North",absoluteMap)
    return absoluteMap


def getSafeLocation(absoluteMap):
    safeLocList = []
    for i,cell in enumerate(absoluteMap):
        if cell[4] == "s":
            for k,v in dictionary.items():
                if(v == i):
                    safeLocList.append((i,k))
   
    return random.choice(safeLocList)



def initializeAgent(safeLoc,fileName,absoluteMap):
    prolog = Prolog()
    prolog.consult(fileName)
    list(prolog.query("reborn"))

    percepts = getPercepts(absoluteMap[dictionary[(1,1)]]) # get initial percept
    percepts[0] = "on"
    print("ppp", safeLoc)
    
    list(prolog.query("reposition({})".format(percepts)))
    return prolog

def getAbsDir(initialAbsDirection, currentDiretion):
    absDirection = ""
    if initialAbsDirection == "north":
        if currentDiretion == "rnorth":
            absDirection = "north"
        elif currentDiretion == "rsouth":
            absDirection = "south"
        elif currentDiretion == "rwest":
            absDirection == "west"
        else:
            absDirection == "east"
    elif initialAbsDirection == "south":
        if currentDiretion == "rnorth":
            absDirection = "south"
        elif currentDiretion == "rsouth":
            absDirection = "north"
        elif currentDiretion =="rwest":
            absDirection = "east"
        else:
            absDirection = "west"
    elif initialAbsDirection == "west":
        if currentDiretion == "rnorth":
            absDirection = "west"
        elif currentDiretion == "rsouth":
            absDirection = "east"
        elif currentDiretion == "rwest":
            absDirection = "north"
        else:
            absDirection = "south"
    elif initialAbsDirection == "east":
        if currentDiretion == "rnorth":
            absDirection = "east"
        elif currentDiretion == "rsouth":
            absDirection = "west"
        elif currentDiretion == "rwest":
            absDirection = "south"
        else:
            absDirection = "north"
    return absDirection

def renewLocForward(currentLocation, initialAbsDirection, currentRelativeLocation):
    #print(initialAbsDirection,currentRelativeLocation["D"])
    absDirection = getAbsDir(initialAbsDirection, currentRelativeLocation["D"])
    (X,Y) = currentLocation
    #print(absDirection)
    if absDirection == "north":
        return (X,Y+1)
    elif absDirection == "south":
        return (X,Y-1)
    elif absDirection == "west":
        return (X-1,Y)
    else:
        return (X+1,Y)

def renewDirLeft(currentAbsDirection):
    if currentAbsDirection == "north":
        return "west"
    elif currentAbsDirection == "south":
        return "east"
    elif currentAbsDirection == "west":
        return "south"
    else:
        return "north"

def renewDirRight(currentAbsDirection):
    if currentAbsDirection == "north":
        return "east"
    elif currentAbsDirection == "south":
        return "west"
    elif currentAbsDirection == "west":
        return "north"
    else:
        return "south"

def getWumpusLocation(absoluteMap):
    for i,cell in enumerate(absoluteMap):
        if cell[4] == "W":
            for k,v in dictionary.items():
                if(v == i):
                    return k

def inSameDirection(wumpusLoc, newAbsLoc, newAbsDir):
    if newAbsDir == "north":
        return wumpusLoc[0] == newAbsLoc[0] and wumpusLoc[1]>newAbsLoc[1]
    elif newAbsDir == "south":
        return wumpusLoc[0] == newAbsLoc[0] and wumpusLoc[1]<newAbsLoc[1]
    elif newAbsDir == "west":
        return wumpusLoc[1] == newAbsLoc[1] and wumpusLoc[0] < newAbsLoc[0]
    else:
        return wumpusLoc[1] == newAbsLoc[1] and wumpusLoc[0] > newAbsLoc[0]

def getAgentWumpus(prolog):
    wumpus = list(prolog.query("wumpus(X,Y)"))
    wumpusList = []
    for item in wumpus:
        wumpusList.append((item["X"],item["Y"]))
    return wumpusList

def getAgentPortal(prolog):
    portal = list(prolog.query("confundus(X,Y)"))
    portalList = []
    for item in portal:
        portalList.append((item["X"],item["Y"]))
    return portalList

def getAgentVisited(prolog):
    visited = list(prolog.query("visited(X,Y)"))
    visitedList = []
    for item in visited:
        visitedList.append((item["X"],item["Y"]))
    return visitedList

def getAgentLocation(prolog):
    loc = list(prolog.query("current(X,Y,D)"))
    return tuple((loc[0]["X"],loc[0]["Y"],loc[0]["D"]))

def getAgentSafe(prolog):
    safe = list(prolog.query("safeToVisit(X,Y)"))
    safeList = []
    for item in safe:
        safeList.append((item["X"],item["Y"]))
    return safeList

def getAgentCoins(prolog):
    coins = list(prolog.query("glitter(X,Y)"))
    coinList = []
    for item in coins:
        coinList.append((item["X"],item["Y"]))
    return coinList

def getAgentStench(prolog):
    stench = list(prolog.query("stench(X,Y)"))
    
    stenchList = []
    for item in stench:
        stenchList.append((item["X"],item["Y"]))
    return stenchList

def getAgentTingle(prolog):
    tingle = list(prolog.query("tingle(X,Y)"))
    tingleList = []
    for item in tingle:
        tingleList.append((item["X"],item["Y"]))
    return tingleList

def getAgentWall(prolog):
    wall = list(prolog.query("wall(X,Y)"))
    wallList = []
    for item in wall:
        wallList.append((item["X"],item["Y"]))
    return wallList

def turnPerceptsToString(perceptList):
    initialString = ""
    if perceptList[0] == "on":
        initialString = initialString + "Confunded-"
    else:
        initialString = initialString + "C-"
    if perceptList[1] == "on":
        initialString = initialString + "Stench-"
    else:
        initialString = initialString + "S-"
    if perceptList[2] == "on":
        initialString = initialString + "Tingle-"
    else:
        initialString = initialString + "T-"
    if perceptList[3] == "on":
        initialString = initialString + "Glitter-"
    else:
        initialString = initialString + "G-"
    if perceptList[4] == "on":
        initialString = initialString + "Bump-"
    else:
        initialString = initialString + "B-"
    if perceptList[5] == "on":
        initialString = initialString + "Scream"
    else:
        initialString = initialString + "S"
    return initialString

def printExploreRelativeMap(prolog,relativeMap):
    possibleWumpus = getAgentWumpus(prolog)
    possiblePortal = getAgentPortal(prolog)
    coins = getAgentCoins(prolog)
    stench = getAgentStench(prolog)
    tingle = getAgentTingle(prolog)
    wall = getAgentWall(prolog)

    safe = getAgentSafe(prolog)
    visited = getAgentVisited(prolog)
    currentAgent = getAgentLocation(prolog)

    direction = currentAgent[2]
    for item in possibleWumpus:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]][4] = "W"
    for item in possiblePortal:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]][4] = "O"
    for item in safe:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]][4] = "s"
    for item in visited:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]][4] = "S"
    for item in coins:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]][6] = "*"
    for item in stench:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]][1] = "="
    for item in tingle:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]][2] = "T"
    for item in wall:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]] = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
    if direction == "rnorth":
        relativeMap[rdictionary[(currentAgent[0]+xOffset,currentAgent[1]+yOffset)]][4] = "∧"
    elif direction == "rsouth":
        relativeMap[rdictionary[(currentAgent[0]+xOffset,currentAgent[1]+yOffset)]][4] = "∨"
    elif direction == "rwest":
        relativeMap[rdictionary[(currentAgent[0]+xOffset,currentAgent[1]+yOffset)]][4] = "<"
    elif direction == "reast":
        relativeMap[rdictionary[(currentAgent[0]+xOffset,currentAgent[1]+yOffset)]][4] = ">"
    relativeMap[rdictionary[(currentAgent[0]+xOffset,currentAgent[1]+yOffset)]][5] = "-"
    printMap("relative", relativeMap)
    relativeMap[rdictionary[(currentAgent[0]+xOffset,currentAgent[1]+yOffset)]][5] = " "

def printLocalizationMap(prolog, relativeMap):
    visited = getAgentVisited(prolog)
    currentAgent = getAgentLocation(prolog)

    for item in visited:
        newItem = (item[0]+xOffset,item[1]+yOffset)
        relativeMap[rdictionary[newItem]][4] = "S"
    relativeMap[rdictionary[(currentAgent[0]+xOffset,currentAgent[1]+yOffset)]][5] = "-"
    printMap("relative", relativeMap)

def takeActions(curLoc,initDir,actionList,prolog,absoluteMap):
    newAbsDir = initDir
    newAbsLoc = curLoc
    
    for action in actionList:
        #print("Current ABS LOCATION", newAbsLoc,newAbsDir)
        relativeMap = createMap("relative")
        action = action.decode('utf-8')
        curRelLoc = list(prolog.query("current(X,Y,D)"))
        curPercepts = getPercepts(absoluteMap[dictionary[newAbsLoc]])
        if curPercepts[3] == "on":
            print("Ask the agent to pick the coin.")
            list(prolog.query("move({},{})".format("pickup", curPercepts)))
        if action == "moveforward":
            oldAbsLoc = newAbsLoc
            newAbsLoc = renewLocForward(newAbsLoc,initDir,curRelLoc[0])
        
            
            if newAbsLoc[0]>=6 or newAbsLoc[0]<=0 or newAbsLoc[1]<=0 or newAbsLoc[1]>=5:
                relativeMap[rdictionary[(curRelLoc[0]["X"]+xOffset,curRelLoc[0]['Y']+yOffset)]][7] = "B"
                index = dictionary[oldAbsLoc]
                percepts= getPercepts(absoluteMap[index]) # there is a wall
                percepts[4] = "on"
                newAbsLoc = oldAbsLoc
                list(prolog.query("move({},{})".format("moveforward", percepts)))
                print("Percepts: ",turnPerceptsToString(percepts))
                print()
                printExploreRelativeMap(prolog,relativeMap)
                relativeMap[rdictionary[(curRelLoc[0]["X"]+xOffset,curRelLoc[0]['Y']+yOffset)]][7] = "."
                continue
            else:
                index = dictionary[newAbsLoc]
                percepts = getPercepts(absoluteMap[index])
                #print("forwardpercepts", absoluteMap[index])
                list(prolog.query("move({},{})".format("moveforward", percepts)))
                
        elif action == "turnleft":
            newAbsDir = renewDirLeft(newAbsDir)
            index = dictionary[newAbsLoc]
            percepts = getPercepts(absoluteMap[index])
            list(prolog.query("move({},{})".format("turnleft", percepts)))
        elif action == "turnright":
            newAbsDir = renewDirRight(newAbsDir)
            index = dictionary[newAbsLoc]
            percepts = getPercepts(absoluteMap[index])
            list(prolog.query("move({},{})".format("turnright", percepts)))
        elif action == "shoot":
            wumpusLoc = getWumpusLocation()
            index = dictionary(newAbsLoc)
            percepts = getPercepts(absoluteMap[index])
            if inSameDirection(wumpusLoc, newAbsLoc, newAbsDir):
                percepts[5] = "on"
                relativeMap[rdictionary[(curRelLoc["X"]+xOffset,curRelLoc['Y']+yOffset)]][8] = "@"
                list(prolog.query("move({},{})".format("shoot", percepts)))
                printExploreRelativeMap(prolog,relativeMap)
                relativeMap[rdictionary[(curRelLoc["X"]+xOffset,curRelLoc['Y']+yOffset)]][8] = "."
            else:
                list(prolog.query("move({},{})".format("shoot", percepts)))

        print(percepts)
        print("Percepts: ",turnPerceptsToString(percepts))
        print()
        printExploreRelativeMap(prolog,relativeMap)
    return newAbsLoc

def endCondition(prolog):
    safe = list(prolog.query("safeToVisit(X,Y)"))
    glitter = list(prolog.query("glitter(X,Y)"))
    loc = list(prolog.query("current(X,Y,D)"))
    if loc[0]["X"]==0 and loc[0]["Y"]==0 and len(safe)==0 and len(glitter)==0:
        return True
    return False

def testLocalization():
    action = ["moveforward", "moveforward", "moveforward", "turnright", "moveforward", "moveforward", "turnright", "moveforward", "moveforward", "moveforward"]
    # Create Empty Map
    absoluteMap = initialize()
    agentOn(1, 1, "North",absoluteMap)
    AGENT_PATH = "Agent.pl"
    safeLoc = getSafeLocation(absoluteMap)
    prolog = initializeAgent(safeLoc,AGENT_PATH,absoluteMap)
    relativeMap = createMap("relative")
    # Initialize Agent
    agentOn(1,1, "North",absoluteMap)
    printMap("absolute",absoluteMap)
    absLoc = (1,1,"north")
    currentLoc = getAgentLocation(prolog)
    relativeMap[rdictionary[(currentLoc[0]+xOffset,currentLoc[1]+yOffset)]][4] = "S"
    relativeMap[rdictionary[(currentLoc[0]+xOffset,currentLoc[1]+yOffset)]][5] = "-"
    
    for i in action:
        # get agent's current direction
        index = dictionary[(absLoc[0],absLoc[1])]
        percepts = getPercepts(absoluteMap[index])
        list(prolog.query("move({},{})".format(i,percepts)))
        print("Action: ", i)
        printLocalizationMap(prolog, relativeMap)

def testExplore():
    # need to change the path
    absoluteMap = initialize()
    AGENT_PATH = "Agent.pl"
    TTL = 8 #Time to live
    safeLoc = getSafeLocation(absoluteMap) #(index,(X,Y))
    Dir = "north"  #can be random
    prolog = initializeAgent(safeLoc,AGENT_PATH,absoluteMap)  
    
    # initialize Agent
    agentOn(1,1, "North",absoluteMap)
    printMap("absolute",absoluteMap)
    print("Agent's current knowledge: ")
    relativeMap = createMap("relative")
    printExploreRelativeMap(prolog,relativeMap)
    L = list(prolog.query("explore(L)"))
    curLoc = (1,1)
    while(len(L[0]['L'])!=0 and TTL>0 and not endCondition(prolog)):
        print("Actions: ", L[0]['L'])
        relativeMap = createMap("relative")
        newCurLoc=takeActions(curLoc,Dir,L[0]['L'],prolog, absoluteMap)
        
        L = list(prolog.query("explore(L)"))
        curLoc = newCurLoc
        TTL = TTL-1
    if len(L[0]['L'])==0:
        print("No more available actions!")
    elif TTL <= 0:
        print("Explore time exceed!")
    elif endCondition(prolog):
        print("Reached end-game status.")
    print("The driver is ending the game. Agent will be reset.")
    list(prolog.query("reborn"))
    print("Agent's current knowledge: (After end-game reset): ")
    relativeMap = createMap("relative")
    printExploreRelativeMap(prolog,relativeMap)


    
def testPortal():
    absoluteMap = initialize()
    AGENT_PATH = "Agent.pl"
    safeLoc = getSafeLocation(absoluteMap) #(index,(X,Y))
    Dir = "north"  #can be random
    prolog = initializeAgent(safeLoc,AGENT_PATH,absoluteMap)  
    relativeMap = createMap("relative")
    printMap("absolute", absoluteMap)
    list(prolog.query("move({},{})".format("turnright",getPercepts(absoluteMap[dictionary[(1, 1)]]))))
    list(prolog.query("move({},{})".format("moveforward",getPercepts(absoluteMap[dictionary[(2, 1)]]))))
    list(prolog.query("move({},{})".format("moveforward",getPercepts(absoluteMap[dictionary[(3, 1)]]))))
    list(prolog.query("move({},{})".format("shoot",getPercepts(absoluteMap[dictionary[(3, 1)]]))))         #the agent loses arrow
    list(prolog.query("move({},{})".format("moveforward",getPercepts(absoluteMap[dictionary[(4, 1)]]))))
    
    print("Agent's current knowledge: ")
    printExploreRelativeMap(prolog,relativeMap)
    print("Does the agent have arrow now? ")
    print(bool(list(prolog.query("hasarrow"))))
    print("Repositing the agent to [2,2].........")
    list(prolog.query("reposition({})".format("[on,off,off,off,off,off]")))

    print("Agent's current knowledge (after reposition): ")
    relativeMap = createMap("relative")
    printExploreRelativeMap(prolog,relativeMap)
    print("Does the agent have arrow now? ")
    print(bool(list(prolog.query("hasarrow"))))



if __name__ == '__main__':

    '''
    Uncomment the test you would like to try.
    '''
    
    print("TESTING LOCALIZING ABILITY")
    print("=========================")
    #testLocalization()
    print("=========================")
    print()
    print()
    print("TESTING EXPLORE/1")
    print("=========================")
    testExplore()
    print("=========================")
    print()
    print()
    print("TESTING REPOSITION/1")
    print("=========================")
    testPortal()
    print("=========================")

