# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from pyswip import *


# 3x3 Map Cell
# 1: Confounded. "%"
# 2: Stench. ”=”
# 3: Tingle. "T"
# 4: ”−” if the cell contains the Agent or an NPC, otherwise prints as a single space.
# 5: "W" for wumpus,
#    "O" for portal,
#    "^", "v" ,"<", ">" for agent,
#    "s" for unvisited safe map cell without agent,
#    "S" for visited safe map cell with agent,
#    "?" if none of the above
# 6: ”−” if the cell contains the Agent or an NPC, otherwise prints as a single space.
# 7: Glitter "*"
# 8: Bump. ”B” is printed if the indicator is on and a dot otherwise.
#    Caution: Bump indicator is transitory. That is, it will appear only if the agent tried to go forward and
#    met a Wall.
# 9: Scream indicator. ”@” is printed if the indicator is on and a dot otherwise.
#    Caution: Scream indicator is transitory. That is, it will appear only if the agent shot its Arrow and
#    the Wumpus was killed/removed.
# Exclusion: If a map cell is inhabited by a (known) Wall, then all symbol are #

# X, Y = (7,6)
# Rows = Y, Cols = X
rows = 6
cols = 7

rrows = (rows*2) - 1
rcols = (cols*2) -1
rMapCell = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

mapCell = [".", ".", ".", " ", "?", " ", ".", ".", "."]
wall = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
absoluteMap = []
relativeMap = []

actionSequence = []



# Co-ordinates to absoluteMap index
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



# Create Map
def createMap(mapType):
    if mapType == "absolute":
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
                if cells[4] == '#':
                    continue
                else:
                    cells[4] = "s"
    elif mapType == "relative":
        for i in range(rrows):
            for j in range(rcols):
                relativeMap.append(rMapCell.copy())


def printMap(mapType, L, position):
    if mapType=="absolute":
        sensory = ""
        if L[0] == "on":
            sensory = "Confounded-"
        else:
            sensory = "C-"
        if L[1] == "on":
            sensory = sensory + "Stench-"
        else:
            sensory = sensory + "S-"
        if L[2] == "on":
            sensory = sensory + "Tingle-"
        else:
            sensory = sensory + "T-"
        if L[3] == "on":
            sensory = sensory + "Glitter-"
        else:
            sensory = sensory + "G-"
        if L[4] == "on":
            sensory = sensory + "Bump-"
        else:
            sensory = sensory + "B-"
        if L[5] == "on":
            sensory = sensory + "Scream"
        else:
            sensory = sensory + "S"
        print("============================================================")
        print("========================ABSOLUTE MAP========================")
        print()
        print(actionSequence)
        print(sensory)
        current = cols
        prev = 0
        total = rows * cols
        while total > 0:
            for i in range(prev, current, 1):
                for j in range(0, 3, 1):
                    print(absoluteMap[i][j], end=" ")
                print(" ", end=" ")
            print()
            for i in range(prev, current, 1):
                for j in range(3, 6, 1):
                    print(absoluteMap[i][j], end=" ")
                print(" ", end=" ")
            print()
            for i in range(prev, current, 1):
                for j in range(6, 9, 1):
                    print(absoluteMap[i][j], end=" ")
                print(" ", end=" ")

            print()
            print()

            prev = current
            current = current + cols
            total = total - cols
        print("============================================================")

    elif mapType=="relative":
        sensory = ""
        if L[0] == "on":
            sensory = "Confounded-"
        else:
            sensory = "C-"
        if L[1] == "on":
            sensory = sensory + "Stench-"
        else:
            sensory = sensory + "S-"
        if L[2] == "on":
            sensory = sensory + "Tingle-"
        else:
            sensory = sensory + "T-"
        if L[3] == "on":
            sensory = sensory + "Glitter-"
        else:
            sensory = sensory + "G-"
        if L[4] == "on":
            sensory = sensory + "Bump-"
        else:
            sensory = sensory + "B-"
        if L[5] == "on":
            sensory = sensory + "Scream"
        else:
            sensory = sensory + "S"
        

        print("============================================================")
        print("========================RELATIVE MAP========================")
        print()
        print(actionSequence)
        print(sensory)
        print("X:", position["rX"], ", Y:", position["rY"], ", Direction:", position["rDir"])
        current = rcols
        prev = 0
        total = rrows * rcols
        while total > 0:
            for i in range(prev, current, 1):
                for j in range(0, 3, 1):
                    print(relativeMap[i][j], end=" ")
                print(" ", end=" ")
            print()
            for i in range(prev, current, 1):
                for j in range(3, 6, 1):
                    print(relativeMap[i][j], end=" ")
                print(" ", end=" ")
            print()
            for i in range(prev, current, 1):
                for j in range(6, 9, 1):
                    print(relativeMap[i][j], end=" ")
                print(" ", end=" ")

            print()
            print()

            prev = current
            current = current + rcols
            total = total - rcols
        print("============================================================")


# populate portal, wumpus, coin
def stenchOn(x, y):
    absoluteMap[dictionary[(x, y)]][1] = "="


def tingleOn(x, y):
    absoluteMap[dictionary[(x, y)]][2] = "T"


def npcOn(x, y):
    absoluteMap[dictionary[(x, y)]][3] = "-"
    absoluteMap[dictionary[(x, y)]][5] = "-"


def wumpusOn(x, y):
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


def portalOn(x, y):
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

def coinOn(x, y):
    print("Placing Coin at: (", x, ",", y, ")")
    absoluteMap[dictionary[(x, y)]][4] = "?"

    # Set Glitter indicator
    absoluteMap[dictionary[(x, y)]][6] = "*"

def agentOn(x, y, dir):
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
    agentPos["rX"] = 0
    agentPos["rY"] = 0
    agentPos["rDir"] = "rnorth"

    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = "-"
    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = "-"

def initialize():
    createMap("absolute")
    createMap("relative")
    print("Initializing Empty Map...")

    wumpusOn(1, 3)
    portalOn(5, 4)
    portalOn(4, 3)
    portalOn(4, 1)
    coinOn(2, 3)
    agentOn(1, 1, "North")
    printMap("absolute")

def firstTestCase():
    #prolog = Prolog()
    action = ["moveforward", "moveforward", "moveforward", "turnright", "moveforward", "moveforward", "turnright", "moveforward", "moveforward", "moveforward"]
    # Create Empty Map
    createMap("absolute")
    createMap("relative")
    # Initialize Agent
    agentOn(1,1, "North")

    for i in action:
        # get agent's current direction
        dir = agentPos["dir"]
        x = agentPos["x"]
        y = agentPos["y"]
        if i == "moveforward":
            if dir == "North":
                # Update map
                index = dictionary.get((x, y))
                absoluteMap[index][3] = "."
                absoluteMap[index][4] = "S"
                absoluteMap[index][5] = "."

                index = dictionary.get((x, y+1))
                if index:
                    # Update Prolog's knowledge base
                    L = getPercepts(absoluteMap[index])
                    # Confounded
                    # Teleport Agent to 1,1,"North"
                    if absoluteMap[index][4] == "O":
                        # Update map
                        absoluteMap[index][3] = " "
                        absoluteMap[index][4] = "O"
                        absoluteMap[index][5] = " "
                        # Reposition Agent in Absolute Map
                        for j in range(len(absoluteMap)):
                            if absoluteMap[j][4] == "S":
                                k = get_key(j)
                                agentOn(k[0], k[1], "North")

                    # Wumpus
                    elif absoluteMap[index][4] == "W":
                        print("KILLED BY WUMPUS")
                        break;
                    
                    # Update Agent's Co-ordinates
                    updateAgent(x, y+1, dir)
                    actionSequence.append(i)
                    # Update Absolute Map
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "^"
                    absoluteMap[index][5] = "-"

                    # Pick up coin if available
                    if L[3] == "on":
                        # pickup
                        actionSequence.append("pickup")
                        # Turn off Glitter
                        absoluteMap[index][6] = "."
                    
                else:
                    # BUMPED INTO WALL
                    # Turn on bump indicator, print map, turn off bump indicator
                    absoluteMap[index][7] = "B"
                    printMap("absolute")
                    print()
                    #printMap("relative")
                    absoluteMap[index][7] = "."
                    # Revert Map
                    index = dictionary.get((agentPos["x"], agentPos["y"]))
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "^"
                    absoluteMap[index][5] = "-"
                    
                    # Update Prolog's knowledge base
                    L = ["off", "off", "off", "off", "on", "off"]
                    # Prolog's move(A,L)
                    #prolog.query("move({}, {})".format(i, L))
                
            elif dir == "East":
                # Update map
                index = dictionary.get((x, y))
                absoluteMap[index][3] = "."
                absoluteMap[index][4] = "S"
                absoluteMap[index][5] = "."

                index = dictionary.get((x+1, y))
                if index:
                    # Update Prolog's knowledge base
                    L = getPercepts(absoluteMap[index])
                    # Prolog's move(A,L)
                    #prolog.query("move({}, {})".format(i, L))

                    # Confounded
                    # Teleport Agent to 1,1,"North"
                    if absoluteMap[index][4] == "O":
                        # Update map
                        absoluteMap[index][3] = " "
                        absoluteMap[index][4] = "O"
                        absoluteMap[index][5] = " "
                        # Reposition Agent in Absolute Map
                        for j in range(len(absoluteMap)):
                            if absoluteMap[j][4] == "S":
                                k = get_key(j)
                                agentOn(k[0], k[1], "North")
                        # Tell Agent to reposition
                        L = getPercepts(absoluteMap[dictionary.get((1,1))])
                        #prolog.query("reposition({})".format(L))

                    # Wumpus
                    elif absoluteMap[index][4] == "W":
                        print("DEAD")
                        # reborn
                        #prolog.query("reborn")
                        break;
                    # Update Agent's Co-ordinates
                    updateAgent(x+1, y, dir)
                    actionSequence.append(i)
                    # Update Absolute Map
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = ">"
                    absoluteMap[index][5] = "-"

                    # Pick up coin if available
                    if L[3] == "on":
                        # tell agent to pickup
                        actionSequence.append("pickup")
                        # Turn off Glitter
                        absoluteMap[index][6] = "."
                else:
                    # BUMPED INTO WALL
                    # Turn on bump indicator, print map, turn off bump indicator
                    absoluteMap[index][7] = "B"
                    printMap("absolute")
                    print()
                    #printMap("relative")
                    absoluteMap[index][7] = "."
                    # Revert Map
                    index = dictionary.get((agentPos["x"], agentPos["y"]))
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = ">"
                    absoluteMap[index][5] = "-"
                    
                    # Update Prolog's knowledge base
                    L = ["off", "off", "off", "off", "on", "off"]
                    # Prolog's move(A,L)
                    #prolog.query("move({}, {})".format(i, L))
            elif dir == "South":
                # Update map
                index = dictionary.get((x, y))
                absoluteMap[index][3] = "."
                absoluteMap[index][4] = "S"
                absoluteMap[index][5] = "."

                index = dictionary.get((x, y-1))
                if index:
                    # Update Prolog's knowledge base
                    L = getPercepts(absoluteMap[index])
                    # Prolog's move(A,L)
                    #prolog.query("move({}, {})".format(i, L))

                    # Confounded
                    # Teleport Agent to 1,1,"North"
                    if absoluteMap[index][4] == "O":
                        # Update map
                        absoluteMap[index][3] = " "
                        absoluteMap[index][4] = "O"
                        absoluteMap[index][5] = " "
                        # Reposition Agent in Absolute Map
                        for j in range(len(absoluteMap)):
                            if absoluteMap[j][4] == "S":
                                k = get_key(j)
                                agentOn(k[0], k[1], "North")
                        # Tell Agent to reposition
                        L = getPercepts(absoluteMap[dictionary.get((1,1))])
                        #prolog.query("reposition({})".format(L))

                    # Wumpus
                    elif absoluteMap[index][4] == "W":
                        print("DEAD")
                        # reborn
                        #prolog.query("reborn")
                        break;
                    
                    # Update Agent's Co-ordinates
                    updateAgent(x, y-1, dir)
                    actionSequence.append(i)
                    # Update Absolute Map
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "v"
                    absoluteMap[index][5] = "-"

                    # Pick up coin if available
                    if L[3] == "on":
                        # tell agent to pickup
                        actionSequence.append("pickup")
                        # Turn off Glitter
                        absoluteMap[index][6] = "."
                else:
                    # BUMPED INTO WALL
                    # Turn on bump indicator, print map, turn off bump indicator
                    absoluteMap[index][7] = "B"
                    printMap("absolute")
                    print()
                    #printMap("relative")
                    absoluteMap[index][7] = "."
                    # Revert Map
                    index = dictionary.get((agentPos["x"], agentPos["y"]))
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "v"
                    absoluteMap[index][5] = "-"
                    
                    # Update Prolog's knowledge base
                    L = ["off", "off", "off", "off", "on", "off"]
                    # Prolog's move(A,L)
                    #prolog.query("move({}, {})".format(i, L))
            elif dir == "West":
                # Update map
                index = dictionary.get((x, y))
                absoluteMap[index][3] = "."
                absoluteMap[index][4] = "S"
                absoluteMap[index][5] = "."

                index = dictionary.get((x-1, y))
                if index:
                    # Update Prolog's knowledge base
                    L = getPercepts(absoluteMap[index])
                    # Prolog's move(A,L)
                    #prolog.query("move({}, {})".format(i, L))

                    # Confounded
                    # Teleport Agent to 1,1,"North"
                    if absoluteMap[index][4] == "O":
                        # Update map
                        absoluteMap[index][3] = " "
                        absoluteMap[index][4] = "O"
                        absoluteMap[index][5] = " "
                        # Reposition Agent in Absolute Map
                        for j in range(len(absoluteMap)):
                            if absoluteMap[j][4] == "S":
                                k = get_key(j)
                                agentOn(k[0], k[1], "North")
                        # Tell Agent to reposition
                        L = getPercepts(absoluteMap[dictionary.get((1,1))])
                        #prolog.query("reposition({})".format(L))

                    # Wumpus
                    elif absoluteMap[index][4] == "W":
                        print("DEAD")
                        # reborn
                        #prolog.query("reborn")
                        break;

                    # Update Agent's Co-ordinates
                    updateAgent(x-1, y, dir)
                    actionSequence.append(i)
                    # Update Absolute Map
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "<"
                    absoluteMap[index][5] = "-"

                    # Pick up coin if available
                    if L[3] == "on":
                        # tell agent to pickup
                        actionSequence.append("pickup")
                        # Turn off Glitter
                        absoluteMap[index][6] = "."
                else:
                    # BUMPED INTO WALL
                    # Turn on bump indicator, print map, turn off bump indicator
                    absoluteMap[index][7] = "B"
                    printMap("absolute")
                    print()
                    #printMap("relative")
                    absoluteMap[index][7] = "."
                    # Revert Map
                    index = dictionary.get((agentPos["x"], agentPos["y"]))
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "<"
                    absoluteMap[index][5] = "-"
                    
                    # Update Prolog's knowledge base
                    L = ["off", "off", "off", "off", "on", "off"]
                    # Prolog's move(A,L)
                    #prolog.query("move({}, {})".format(i, L))
        elif i == "turnleft":
            if dir == "North":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "<"
                updateAgent(x, y, "West")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                #prolog.query("move({}, {})".format(i, L))
                
            elif dir == "East":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "^"
                updateAgent(x, y, "North")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                #prolog.query("move({}, {})".format(i, L))
                
            elif dir == "South":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = ">"
                updateAgent(x, y, "East")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                #prolog.query("move({}, {})".format(i, L))
                
            elif dir == "West":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "v"
                updateAgent(x, y, "South")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                #prolog.query("move({}, {})".format(i, L))

        elif i == "turnright":
            if dir == "North":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = ">"
                updateAgent(x, y, "East")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                #prolog.query("move({}, {})".format(i, L))

            elif dir == "East":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "v"
                updateAgent(x, y, "South")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                #prolog.query("move({}, {})".format(i, L))
                
            elif dir == "South":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "<"
                updateAgent(x, y, "West")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                #prolog.query("move({}, {})".format(i, L))
               
            elif dir == "West":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "^"
                updateAgent(x, y, "North")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                #prolog.query("move({}, {})".format(i, L))

            
        elif i == "shoot":
            index = dictionary.get((x, y))
            actionSequence.append(i)
            if dir == "North":
                tempIndex = 1
                tempY = y
                while tempIndex:
                    tempY += 1
                    tempIndex = dictionary.get((x, tempY))
                    if tempIndex:
                        # Check for Wumpus
                        if absoluteMap[tempIndex][4] == "W":
                            # Scream Indicator On
                            absoluteMap[index][8] = "@"
                            printMap("absolute")
                            print()
                            #printMap("relative")
                            # Update Prolog's knowledge base
                            L = getPercepts(absoluteMap[index])
                            # Prolog's move(A,L)
                            #prolog.query("move({}, {})".format(i, L))
                            # Scream Indicator Off
                            absoluteMap[index][8] = "."
                            printMap("absolute")
                            print()
                            #printMap("relative")

            elif dir == "East":
                tempIndex = 1
                tempX = x
                while tempIndex:
                    tempX += 1
                    tempIndex = dictionary.get((tempX, y))
                    if tempIndex:
                        # Check for Wumpus
                        if absoluteMap[tempIndex][4] == "W":
                            # Scream Indicator On
                            absoluteMap[index][8] = "@"
                            printMap("absolute")
                            print()
                            #printMap("relative")
                            # Update Prolog's knowledge base
                            L = getPercepts(absoluteMap[index])
                            # Prolog's move(A,L)
                            #prolog.query("move({}, {})".format(i, L))
                            # Scream Indicator Off
                            absoluteMap[index][8] = "."
                            printMap("absolute")
                            print()
                            #printMap("relative")
            elif dir == "South":
                tempIndex = 1
                tempY = y
                while tempIndex:
                    tempY -= 1
                    tempIndex = dictionary.get((x, tempY))
                    if tempIndex:
                        # Check for Wumpus
                        if absoluteMap[tempIndex][4] == "W":
                            # Scream Indicator On
                            absoluteMap[index][8] = "@"
                            printMap("absolute")
                            print()
                            #printMap("relative")
                            # Update Prolog's knowledge base
                            L = getPercepts(absoluteMap[index])
                            # Prolog's move(A,L)
                            #prolog.query("move({}, {})".format(i, L))
                            # Scream Indicator Off
                            absoluteMap[index][8] = "."
                            printMap("absolute")
                            print()
                            #printMap("relative")
            elif dir == "West":
                tempIndex = 1
                tempX = x
                while tempIndex:
                    tempX -= 1
                    tempIndex = dictionary.get((tempX, y))
                    if tempIndex:
                        # Check for Wumpus
                        if absoluteMap[tempIndex][4] == "W":
                            # Scream Indicator On
                            absoluteMap[index][8] = "@"
                            printMap("absolute")
                            print()
                            #printMap("relative")
                            # Update Prolog's knowledge base
                            L = getPercepts(absoluteMap[index])
                            # Prolog's move(A,L)
                            #prolog.query("move({}, {})".format(i, L))
                            # Scream Indicator Off
                            absoluteMap[index][8] = "."
                            printMap("absolute")
                            print()
                            #printMap("relative")

        # Print Map
        printMap("absolute")
        print()
        #printMap("relative")

def secondTestCase():
    prolog = Prolog()
    prolog.consult("Agent.pl")
    list(prolog.query("reposition([on,off,off,off,off,off])"))
    action = ["moveforward", "moveforward", "moveforward", "turnright", "moveforward", "moveforward", "turnright", "moveforward", "moveforward", "moveforward"]
    # Create Empty Map
    createMap("absolute")
    createMap("relative")
    # Initialize Agent
    agentOn(1,1, "North")
    #action = list(prolog.query("explore(L)"))

    for i in action:
        # get agent's current direction
        dir = agentPos["dir"]
        x = agentPos["x"]
        y = agentPos["y"]
        
        if i == "moveforward":
            if dir == "North":
                # Update map
                index = dictionary.get((x, y))
                absoluteMap[index][3] = "."
                absoluteMap[index][4] = "S"
                absoluteMap[index][5] = "."
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][0] = absoluteMap[index][0]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][1] = absoluteMap[index][1]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][2] = absoluteMap[index][2]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][6] = absoluteMap[index][6]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][7] = absoluteMap[index][7]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][8] = absoluteMap[index][8]

                index = dictionary.get((x, y+1))
                if index:
                    # Update Prolog's knowledge base
                    L = getPercepts(absoluteMap[index])
                    # Prolog's move(A,L)
                    list(prolog.query("move({}, {})".format(i, L)))
                    
                    # Confounded
                    # Teleport Agent to 1,1,"North"
                    if absoluteMap[index][4] == "O":
                        # Update map
                        absoluteMap[index][3] = " "
                        absoluteMap[index][4] = "O"
                        absoluteMap[index][5] = " "
                        # Reposition Agent in Absolute Map
                        for j in range(len(absoluteMap)):
                            if absoluteMap[j][4] == "S":
                                k = get_key(j)
                                agentOn(k[0], k[1], "North")
                        # Tell Agent to reposition
                        L = getPercepts(absoluteMap[dictionary.get((1,1))])
                        list(prolog.query("reposition({})".format(L)))

                    # Wumpus
                    elif absoluteMap[index][4] == "W":
                        print("Killed by Wumpus")
                        # reborn
                        list(prolog.query("reborn"))
                        break;

                    actionSequence.append(i)
                    # Pick up coin if available
                    if L[3] == "on":
                        # tell agent to pickup
                        list(prolog.query("move({}, {})".format("pickup", L)))
                        # Turn off Glitter
                        absoluteMap[index][6] = "."
                        actionSequence.append("pickup")
                    
                    # Update Agent's Co-ordinates
                    updateAgent(x, y+1, dir)
                    
                    # Update Absolute Map
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "^"
                    absoluteMap[index][5] = "-"

                    relativePos = list(prolog.query("current(X,Y,D)"))
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][0] = absoluteMap[index][0]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][1] = absoluteMap[index][1]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][2] = absoluteMap[index][2]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][6] = absoluteMap[index][6]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][7] = absoluteMap[index][7]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][8] = absoluteMap[index][8]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = " "
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "S"
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = " "
                    
                    agentPos["rX"] = relativePos[0]['X']
                    agentPos["rY"] = relativePos[0]['Y']
                    agentPos["rDir"] = relativePos[0]['D']

                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = "-"
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = "-"
                    if agentPos["rDir"] == "rnorth":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                    elif agentPos["rDir"] == "reast":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                    elif agentPos["rDir"] == "rsouth":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                    elif agentPos["rDir"] == "rwest":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
                    
                else:
                    # BUMPED INTO WALL
                    # Turn on bump indicator, print map, turn off bump indicator
                    absoluteMap[index][7] = "B"
                    printMap("absolute")
                    print()
                    printMap("relative")
                    absoluteMap[index][7] = "."
                    # Revert Map
                    index = dictionary.get((agentPos["x"], agentPos["y"]))
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "^"
                    absoluteMap[index][5] = "-"
                    
                    # Update Prolog's knowledge base
                    L = ["off", "off", "off", "off", "on", "off"]
                    # Prolog's move(A,L)
                    list(prolog.query("move({}, {})".format(i, L)))

                    for eac in range(9):
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, (agentPos["rY"]+1)+yOffset)]][eac] = "#"
                    
                
            elif dir == "East":
                # Update map
                index = dictionary.get((x, y))
                absoluteMap[index][3] = "."
                absoluteMap[index][4] = "S"
                absoluteMap[index][5] = "."
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][0] = absoluteMap[index][0]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][1] = absoluteMap[index][1]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][2] = absoluteMap[index][2]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][6] = absoluteMap[index][6]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][7] = absoluteMap[index][7]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][8] = absoluteMap[index][8]

                index = dictionary.get((x+1, y))
                if index:
                    # Update Prolog's knowledge base
                    L = getPercepts(absoluteMap[index])
                    # Prolog's move(A,L)
                    list(prolog.query("move({}, {})".format(i, L)))
                    
                    # Confounded
                    # Teleport Agent to 1,1,"North"
                    if absoluteMap[index][4] == "O":
                        # Update map
                        absoluteMap[index][3] = " "
                        absoluteMap[index][4] = "O"
                        absoluteMap[index][5] = " "
                        # Reposition Agent in Absolute Map
                        for j in range(len(absoluteMap)):
                            if absoluteMap[j][4] == "S":
                                k = get_key(j)
                                agentOn(k[0], k[1], "North")
                        # Tell Agent to reposition
                        L = getPercepts(absoluteMap[dictionary.get((1,1))])
                        list(prolog.query("reposition({})".format(L)))

                    # Wumpus
                    elif absoluteMap[index][4] == "W":
                        print("Killed by Wumpus")
                        # reborn
                        list(prolog.query("reborn"))
                        break;

                    actionSequence.append(i)
                    # Pick up coin if available
                    if L[3] == "on":
                        # tell agent to pickup
                        list(prolog.query("move({}, {})".format("pickup", L)))
                        # Turn off Glitter
                        absoluteMap[index][6] = "."
                        actionSequence.append("pickup")
                    
                    # Update Agent's Co-ordinates
                    updateAgent(x+1, y, dir)
                    # Update Absolute Map
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = ">"
                    absoluteMap[index][5] = "-"

                    relativePos = list(prolog.query("current(X,Y,D)"))
                    
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = " "
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "S"
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = " "
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][0] = absoluteMap[index][0]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][1] = absoluteMap[index][1]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][2] = absoluteMap[index][2]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][6] = absoluteMap[index][6]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][7] = absoluteMap[index][7]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][8] = absoluteMap[index][8]

                    agentPos["rX"] = relativePos[0]['X']
                    agentPos["rY"] = relativePos[0]['Y']
                    agentPos["rDir"] = relativePos[0]['D']

                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = "-"
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = "-"
                    if agentPos["rDir"] == "rnorth":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                    elif agentPos["rDir"] == "reast":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                    elif agentPos["rDir"] == "rsouth":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                    elif agentPos["rDir"] == "rwest":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
                else:
                    # BUMPED INTO WALL
                    # Turn on bump indicator, print map, turn off bump indicator
                    absoluteMap[index][7] = "B"
                    printMap("absolute")
                    print()
                    printMap("relative")
                    absoluteMap[index][7] = "."
                    # Revert Map
                    index = dictionary.get((agentPos["x"], agentPos["y"]))
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = ">"
                    absoluteMap[index][5] = "-"
                    
                    # Update Prolog's knowledge base
                    L = ["off", "off", "off", "off", "on", "off"]
                    # Prolog's move(A,L)
                    list(prolog.query("move({}, {})".format(i, L)))

                    for eac in range(9):
                        relativeMap[rdictionary[((agentPos["rX"]+1)+xOffset, agentPos["rY"]+yOffset)]][eac] = "#"
            elif dir == "South":
                # Update map
                index = dictionary.get((x, y))
                absoluteMap[index][3] = "."
                absoluteMap[index][4] = "S"
                absoluteMap[index][5] = "."
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][0] = absoluteMap[index][0]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][1] = absoluteMap[index][1]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][2] = absoluteMap[index][2]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][6] = absoluteMap[index][6]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][7] = absoluteMap[index][7]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][8] = absoluteMap[index][8]
                index = dictionary.get((x, y-1))
                if index:
                    # Update Prolog's knowledge base
                    L = getPercepts(absoluteMap[index])
                    # Prolog's move(A,L)
                    list(prolog.query("move({}, {})".format(i, L)))
                    
                    # Confounded
                    # Teleport Agent to 1,1,"North"
                    if absoluteMap[index][4] == "O":
                        # Update map
                        absoluteMap[index][3] = " "
                        absoluteMap[index][4] = "O"
                        absoluteMap[index][5] = " "
                        # Reposition Agent in Absolute Map
                        for j in range(len(absoluteMap)):
                            if absoluteMap[j][4] == "S":
                                k = get_key(j)
                                agentOn(k[0], k[1], "North")
                        # Tell Agent to reposition
                        L = getPercepts(absoluteMap[dictionary.get((1,1))])
                        list(prolog.query("reposition({})".format(L)))

                    # Wumpus
                    elif absoluteMap[index][4] == "W":
                        print("Killed by Wumpus")
                        # reborn
                        list(prolog.query("reborn"))
                        break;

                    actionSequence.append(i)
                    # Pick up coin if available
                    if L[3] == "on":
                        # tell agent to pickup
                        list(prolog.query("move({}, {})".format("pickup", L)))
                        # Turn off Glitter
                        absoluteMap[index][6] = "."
                        actionSequence.append("pickup")
                    
                    # Update Agent's Co-ordinates
                    updateAgent(x, y-1, dir)
                    # Update Absolute Map
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "v"
                    absoluteMap[index][5] = "-"

                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][0] = absoluteMap[index][0]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][1] = absoluteMap[index][1]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][2] = absoluteMap[index][2]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][6] = absoluteMap[index][6]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][7] = absoluteMap[index][7]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][8] = absoluteMap[index][8]

                    relativePos = list(prolog.query("current(X,Y,D)"))
                    
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = " "
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "S"
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = " "

                    agentPos["rX"] = relativePos[0]['X']
                    agentPos["rY"] = relativePos[0]['Y']
                    agentPos["rDir"] = relativePos[0]['D']

                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = "-"
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = "-"
                    if agentPos["rDir"] == "rnorth":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                    elif agentPos["rDir"] == "reast":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                    elif agentPos["rDir"] == "rsouth":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                    elif agentPos["rDir"] == "rwest":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
                else:
                    # BUMPED INTO WALL
                    # Turn on bump indicator, print map, turn off bump indicator
                    absoluteMap[index][7] = "B"
                    printMap("absolute")
                    print()
                    printMap("relative")
                    absoluteMap[index][7] = "."
                    # Revert Map
                    index = dictionary.get((agentPos["x"], agentPos["y"]))
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "v"
                    absoluteMap[index][5] = "-"
                    
                    
                    # Update Prolog's knowledge base
                    L = ["off", "off", "off", "off", "on", "off"]
                    # Prolog's move(A,L)
                    list(prolog.query("move({}, {})".format(i, L)))
                    for eac in range(9):
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, (agentPos["rY"]-1)+yOffset)]][eac] = "#"
            elif dir == "West":
                # Update map
                index = dictionary.get((x, y))
                absoluteMap[index][3] = "."
                absoluteMap[index][4] = "S"
                absoluteMap[index][5] = "."
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][0] = absoluteMap[index][0]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][1] = absoluteMap[index][1]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][2] = absoluteMap[index][2]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][6] = absoluteMap[index][6]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][7] = absoluteMap[index][7]
                relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][8] = absoluteMap[index][8]

                index = dictionary.get((x-1, y))
                if index:
                    # Update Prolog's knowledge base
                    L = getPercepts(absoluteMap[index])
                    # Prolog's move(A,L)
                    list(prolog.query("move({}, {})".format(i, L)))
                    
                    # Confounded
                    # Teleport Agent to 1,1,"North"
                    if absoluteMap[index][4] == "O":
                        # Update map
                        absoluteMap[index][3] = " "
                        absoluteMap[index][4] = "O"
                        absoluteMap[index][5] = " "
                        # Reposition Agent in Absolute Map
                        for j in range(len(absoluteMap)):
                            if absoluteMap[j][4] == "S":
                                k = get_key(j)
                                agentOn(k[0], k[1], "North")
                        # Tell Agent to reposition
                        L = getPercepts(absoluteMap[dictionary.get((1,1))])
                        list(prolog.query("reposition({})".format(L)))

                    # Wumpus
                    elif absoluteMap[index][4] == "W":
                        print("Killed by Wumpus")
                        # reborn
                        list(prolog.query("reborn"))
                        break;

                    actionSequence.append(i)
                    # Pick up coin if available
                    if L[3] == "on":
                        # tell agent to pickup
                        list(prolog.query("move({}, {})".format("pickup", L)))
                        # Turn off Glitter
                        absoluteMap[index][6] = "."
                        actionSequence.append("pickup")
                    
                    # Update Agent's Co-ordinates
                    updateAgent(x-1, y, dir)
                    # Update Absolute Map
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "<"
                    absoluteMap[index][5] = "-"

                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][0] = absoluteMap[index][0]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][1] = absoluteMap[index][1]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][2] = absoluteMap[index][2]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][6] = absoluteMap[index][6]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][7] = absoluteMap[index][7]
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][8] = absoluteMap[index][8]

                    relativePos = list(prolog.query("current(X,Y,D)"))
                    
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = " "
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "S"
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = " "

                    agentPos["rX"] = relativePos[0]['X']
                    agentPos["rY"] = relativePos[0]['Y']
                    agentPos["rDir"] = relativePos[0]['D']

                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][3] = "-"
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][5] = "-"
                    if agentPos["rDir"] == "rnorth":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                    elif agentPos["rDir"] == "reast":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                    elif agentPos["rDir"] == "rsouth":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                    elif agentPos["rDir"] == "rwest":
                        relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
                else:
                    # BUMPED INTO WALL
                    # Turn on bump indicator, print map, turn off bump indicator
                    absoluteMap[index][7] = "B"
                    printMap("absolute")
                    print()
                    printMap("relative")
                    absoluteMap[index][7] = "."
                    # Revert Map
                    index = dictionary.get((agentPos["x"], agentPos["y"]))
                    absoluteMap[index][3] = "-"
                    absoluteMap[index][4] = "<"
                    absoluteMap[index][5] = "-"
                    
                    # Update Prolog's knowledge base
                    L = ["off", "off", "off", "off", "on", "off"]
                    # Prolog's move(A,L)
                    list(prolog.query("move({}, {})".format(i, L)))
                    for eac in range(9):
                        relativeMap[rdictionary[((agentPos["rX"]-1)+xOffset, agentPos["rY"]+yOffset)]][eac] = "#"
        elif i == "turnleft":
            if dir == "North":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "<"
                updateAgent(x, y, "West")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                list(prolog.query("move({}, {})".format(i, L)))
                
                relativePos = list(prolog.query("current(X,Y,D)"))
                agentPos["rDir"] = relativePos[0]['D']

                if agentPos["rDir"] == "rnorth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                elif agentPos["rDir"] == "reast":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                elif agentPos["rDir"] == "rsouth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                elif agentPos["rDir"] == "rwest":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
                
            elif dir == "East":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "^"
                updateAgent(x, y, "North")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                list(prolog.query("move({}, {})".format(i, L)))
                
                relativePos = list(prolog.query("current(X,Y,D)"))
                agentPos["rDir"] = relativePos[0]['D']

                if agentPos["rDir"] == "rnorth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                elif agentPos["rDir"] == "reast":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                elif agentPos["rDir"] == "rsouth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                elif agentPos["rDir"] == "rwest":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
                
            elif dir == "South":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = ">"
                updateAgent(x, y, "East")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                list(prolog.query("move({}, {})".format(i, L)))
                
                relativePos = list(prolog.query("current(X,Y,D)"))
                agentPos["rDir"] = relativePos[0]['D']

                if agentPos["rDir"] == "rnorth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                elif agentPos["rDir"] == "reast":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                elif agentPos["rDir"] == "rsouth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                elif agentPos["rDir"] == "rwest":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
                
            elif dir == "West":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "v"
                updateAgent(x, y, "South")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                list(prolog.query("move({}, {})".format(i, L)))
                
                relativePos = list(prolog.query("current(X,Y,D)"))
                agentPos["rDir"] = relativePos[0]['D']

                if agentPos["rDir"] == "rnorth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                elif agentPos["rDir"] == "reast":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                elif agentPos["rDir"] == "rsouth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                elif agentPos["rDir"] == "rwest":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"

        elif i == "turnright":
            if dir == "North":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = ">"
                updateAgent(x, y, "East")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                list(prolog.query("move({}, {})".format(i, L)))
                           
                relativePos = list(prolog.query("current(X,Y,D)"))
                agentPos["rDir"] = relativePos[0]['D']

                if agentPos["rDir"] == "rnorth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                elif agentPos["rDir"] == "reast":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                elif agentPos["rDir"] == "rsouth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                elif agentPos["rDir"] == "rwest":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"


            elif dir == "East":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "v"
                updateAgent(x, y, "South")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                list(prolog.query("move({}, {})".format(i, L)))
                
                relativePos = list(prolog.query("current(X,Y,D)"))
                agentPos["rDir"] = relativePos[0]['D']

                if agentPos["rDir"] == "rnorth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                elif agentPos["rDir"] == "reast":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                elif agentPos["rDir"] == "rsouth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                elif agentPos["rDir"] == "rwest":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
                
            elif dir == "South":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "<"
                updateAgent(x, y, "West")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                list(prolog.query("move({}, {})".format(i, L)))
                
                relativePos = list(prolog.query("current(X,Y,D)"))
                agentPos["rDir"] = relativePos[0]['D']

                if agentPos["rDir"] == "rnorth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                elif agentPos["rDir"] == "reast":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                elif agentPos["rDir"] == "rsouth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                elif agentPos["rDir"] == "rwest":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"
               
            elif dir == "West":
                # Update Map
                index = dictionary.get((x, y))
                absoluteMap[index][4] = "^"
                updateAgent(x, y, "North")
                actionSequence.append(i)
                # Update Prolog's knowledge base
                L = getPercepts(absoluteMap[index])
                # Prolog's move(A,L)
                list(prolog.query("move({}, {})".format(i, L)))
                
                relativePos = list(prolog.query("current(X,Y,D)"))
                agentPos["rDir"] = relativePos[0]['D']

                if agentPos["rDir"] == "rnorth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "^"
                elif agentPos["rDir"] == "reast":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = ">"
                elif agentPos["rDir"] == "rsouth":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "v"
                elif agentPos["rDir"] == "rwest":
                    relativeMap[rdictionary[(agentPos["rX"]+xOffset, agentPos["rY"]+yOffset)]][4] = "<"

            
        elif i == "shoot":
            index = dictionary.get((x, y))
            actionSequence.append(i)
            if dir == "North":
                tempIndex = 1
                tempY = y
                while tempIndex:
                    tempY += 1
                    tempIndex = dictionary.get((x, tempY))
                    if tempIndex:
                        # Check for Wumpus
                        if absoluteMap[tempIndex][4] == "W":
                            # Scream Indicator On
                            absoluteMap[index][8] = "@"
                            printMap("absolute")
                            print()
                            printMap("relative")
                            # Update Prolog's knowledge base
                            L = getPercepts(absoluteMap[index])
                            # Prolog's move(A,L)
                            list(prolog.query("move({}, {})".format(i, L)))
                            # Scream Indicator Off
                            absoluteMap[index][8] = "."
                            printMap("absolute")
                            print()
                            printMap("relative")

            elif dir == "East":
                tempIndex = 1
                tempX = x
                while tempIndex:
                    tempX += 1
                    tempIndex = dictionary.get((tempX, y))
                    if tempIndex:
                        # Check for Wumpus
                        if absoluteMap[tempIndex][4] == "W":
                            # Scream Indicator On
                            absoluteMap[index][8] = "@"
                            printMap("absolute")
                            print()
                            printMap("relative")
                            # Update Prolog's knowledge base
                            L = getPercepts(absoluteMap[index])
                            # Prolog's move(A,L)
                            list(prolog.query("move({}, {})".format(i, L)))
                            # Scream Indicator Off
                            absoluteMap[index][8] = "."
                            printMap("absolute")
                            print()
                            printMap("relative")
            elif dir == "South":
                tempIndex = 1
                tempY = y
                while tempIndex:
                    tempY -= 1
                    tempIndex = dictionary.get((x, tempY))
                    if tempIndex:
                        # Check for Wumpus
                        if absoluteMap[tempIndex][4] == "W":
                            # Scream Indicator On
                            absoluteMap[index][8] = "@"
                            printMap("absolute")
                            print()
                            printMap("relative")
                            # Update Prolog's knowledge base
                            L = getPercepts(absoluteMap[index])
                            # Prolog's move(A,L)
                            list(prolog.query("move({}, {})".format(i, L)))
                            # Scream Indicator Off
                            absoluteMap[index][8] = "."
                            printMap("absolute")
                            print()
                            printMap("relative")
            elif dir == "West":
                tempIndex = 1
                tempX = x
                while tempIndex:
                    tempX -= 1
                    tempIndex = dictionary.get((tempX, y))
                    if tempIndex:
                        # Check for Wumpus
                        if absoluteMap[tempIndex][4] == "W":
                            # Scream Indicator On
                            absoluteMap[index][8] = "@"
                            printMap("absolute")
                            print()
                            printMap("relative")
                            # Update Prolog's knowledge base
                            L = getPercepts(absoluteMap[index])
                            # Prolog's move(A,L)
                            list(prolog.query("move({}, {})".format(i, L)))
                            # Scream Indicator Off
                            absoluteMap[index][8] = "."
                            printMap("absolute")
                            print()
                            printMap("relative")

        # Print Map
        index = dictionary.get((agentPos["x"], agentPos["y"]))
        L = getPercepts(absoluteMap[index])
        #output = list(prolog.query("current(X,Y,D)"))
        printMap("absolute", L, agentPos)
        print()
        printMap("relative", L, agentPos)
    

def thirdTestCase():
    pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    print("FIRST TEST CASE")
    firstTestCase()
    print("=========================")
    '''
    
    print("SECOND TEST CASE")
    secondTestCase()
    print("=========================")
    '''
    print("THIRD TEST CASE")
    thirdTestCase()
    '''
    
    

    



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
