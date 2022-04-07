# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from pyswip import Prolog

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

mapCell = [".", ".", ".", " ", "?", " ", ".", ".", "."]
wall = ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
absoluteMap = []

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


# Create Map
def createMap():
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


def printMap():
    current = cols  # 7
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
    print("===========================================================")


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
    absoluteMap[dictionary[(x, y)]][4] = "G"

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

def initialize():
    createMap()
    print("Initializing Empty Map...")

    wumpusOn(1, 3)
    portalOn(5, 4)
    portalOn(4, 3)
    portalOn(4, 1)
    coinOn(2, 3)
    agentOn(1, 1, "North")
    printMap()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prolog = Prolog()
    prolog.consult("Agent.pl")

    # Initialize the map with Wumpus, Portals, Coin and Agent
    initialize()
    
    

    



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
