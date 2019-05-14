import math

class Node:
    def __init__(self, pos, moves):
        self.pos = pos  #"pos" has double abbrev. meaning: "possible positions"
        self.posLen = len(pos) #the length of pos. goal is reached when possize is 1
        self.moves = moves
        self.movesLen = len(moves)
        self.h = math.floor(math.log(self.posLen, 2))
        #heuristic: an underestimate of # of moves it will take to compress pos to size 1, 
        #if the number of states is reduced by at most half each round.

def turnMazeIntoData():
    #we number all of the squares in the maze: 35 x 35 = 1225
    #since the same pattern is basically translated 9 times, account for that.
    

    #original pattern
    pattern0 = [0,1,2,3,4,5,6,7,8,9,10,
                    36,41,46,
                    72 , 74 ,75 ,76 ,77 ,78 ,79 ,80 ,82 ,
                    108,110,116,118,
                    144, 146, 148,149,150, 152, 154,
                    180, 182, 184,185,186, 188, 190,
                    216, 218, 220,221,222, 224, 226,
                    252, 254, 257, 260, 262,
                    288, 290,291,292,293,294,295,296,298, 
                    324, 334,
                    360,361,362,363,364,365,366,367,368,369,370
                    ]

    patterns = [[] for i in range(9)]
    patterns[0] = pattern0

    patterns[1] = [x+12 for x in patterns[0]]
    patterns[2] = [x+12 for x in patterns[1]]
    patterns[3] = [x+432 for x in patterns[0]]
    patterns[4] = [x+432 for x in patterns[1]]
    patterns[5] = [x+432 for x in patterns[2]]
    patterns[6] = [x+432 for x in patterns[3]]
    patterns[7] = [x+432 for x in patterns[4]]
    patterns[8] = [x+432 for x in patterns[5]]

    x0 = [371, 406, 407, 408, 443]
    xs = [[] for i in range(4)]
    xs[0] = x0

    xs[1] = [x+12 for x in xs[0]]
    xs[2] = [x+ (36*12) for x in xs[0]]
    xs[3] = [x+ (36*12) for x in xs[1]]

    totalMaze = []

    for p in patterns:
        for n in p:
            totalMaze.append(n)

    for x in xs:
        for n in x:
            totalMaze.append(n)

    totalMaze.sort()

    totalMaze = list(dict.fromkeys(totalMaze))

    #print(len(totalMaze))
    return totalMaze

    #perform 

def turnMazeListToDict(maze):
    dic = {}
    for m in maze:
        dic[m] = 0
    return dic

def moveUpAndReduce(node, fullMaze): #fullMaze is dict of all empty positions
    maze = node.pos

    newMaze = []
    for num in maze:
        newNum = num -36
        if newNum in fullMaze:
            newMaze.append(newNum)
        else:
            newMaze.append(num)

    newMaze = list(dict.fromkeys(newMaze))

    newNode = Node(newMaze, node.moves + "U")
    return newNode
 
def moveDownAndReduce(node, fullMaze): #fullMaze is dict of all empty positions
    maze = node.pos
    
    newMaze = []
    for num in maze:
        newNum = num +36
        if newNum in fullMaze:
            newMaze.append(newNum)
        else:
            newMaze.append(num)

    newMaze = list(dict.fromkeys(newMaze))

    newNode = Node(newMaze, node.moves + "D")
    return newNode
                      

def moveLeftAndReduce(node, fullMaze): #fullMaze is dict of all empty positions
    maze = node.pos 

    newMaze = []
    for num in maze:
        newNum = num -1
        if newNum in fullMaze:
            newMaze.append(newNum)
        else:
            newMaze.append(num)

    newMaze = list(dict.fromkeys(newMaze))

    newNode = Node(newMaze, node.moves + "L")
    return newNode            

def moveRightAndReduce(node, fullMaze): #fullMaze is dict of all empty positions
    maze = node.pos

    newMaze = []
    for num in maze:
        newNum = num +1
        if newNum in fullMaze:
            newMaze.append(newNum)
        else:
            newMaze.append(num)

    newMaze = list(dict.fromkeys(newMaze))

    newNode = Node(newMaze, node.moves + "R")
    return newNode
    

if __name__ == "__main__":

    #this tells us which spaces in the maze are not blocked. DON'T CHANGE THIS DATA
    maze = turnMazeIntoData()   

    #this is the previous data, but faster access using a dict
    mazeDict = turnMazeListToDict(maze)

    print(len(mazeDict))
    print(maze)
    #do the DO

    states = []
    first = Node(maze, "")

    states.append(moveUpAndReduce(first, mazeDict))
    states.append(moveDownAndReduce(first, mazeDict))
    states.append(moveRightAndReduce(first, mazeDict))
    states.append(moveLeftAndReduce(first, mazeDict))

    target = 0
    while True:
        target = 0
        for i in range(len(states)):
            maze = states[i]
            #find the maze that we want to expand...
            if (maze.movesLen + maze.h) < (states[target].movesLen + states[target].h):
                target = i

        #we have found the maze we want to expand. 
        expandMe = states.pop(target)
        
        if expandMe.posLen == 1:
            break
        else:
            print("expand len is: " + str(expandMe.posLen))
            print("expand move len is: " + str(expandMe.movesLen))
            
        states.append(moveUpAndReduce(expandMe, mazeDict))
        states.append(moveDownAndReduce(expandMe, mazeDict))
        states.append(moveRightAndReduce(expandMe, mazeDict))
        states.append(moveLeftAndReduce(expandMe, mazeDict))

    print(states[target].moves)
    
















    
