import sys
import linecache
x = []
y = []
angle = []



#we get the coordinates from a given waypoint position

def cutCoord(initialPos):  #===============================================================================

    prevCount = 0
    angle=[]
    x=[]
    y=[]
    for i in range(0, len(initialPos)):

        if (initialPos[i] == " "):
            prevCount = i + 1
            break

        else :
            x.append(initialPos[i])


    for i in range(prevCount, len(initialPos)):

        if (initialPos[i] == " "):
            prevCount = i+1
            break

        else :
            y.append(initialPos[i])



    for i in range(prevCount, len(initialPos)):

        if (initialPos[i] == " "):
            break

        else :
            angle.append(initialPos[i])

    if (angle[len(angle)-1] == '\n'):
        del angle[len(angle)-1]




    return x, y, angle




def convertCoord(list):    #======================================================================

    x1=list[0]
    y1=list[1]
    angle1=list[2]


    if (len(x1) == 1):
        xVal = int(x1[0])

    elif (len(x1) == 2):
        if (x1[0] == '-'):
           xVal = int(x1[1])*(-1)

        else:
            xVal = int(x1[0])*10 + int(x1[1])



    elif (len(x1) == 3):
        if (x1[0]=='-'):
           xVal = (int(x1[1])*10 + int(x1[2]))*(-1)

        else:
            xVal = int(x1[0])*100 + int(x1[1])*10 + int(x1[2])

    elif (len(x1) == 4):
        if (x1[0]=='-'):
            xVal = (int(y1[1])*100 + int(x1[2])*10 + int(x1[3]))*(-1)

        else:
            xVal = int(x1[0])*1000 + int(x1[1])*100 + int(x1[2])*10 + int(x1[3])


    if (len(y1) == 1):
        yVal = int(y1[0])


    elif (len(y1) == 2):
        if (y1[0] == '-'):
           yVal = int(y1[1])*(-1)

        else:
            yVal = int(y1[0])*10 + int(y1[1])


    elif (len(y1) == 3):
        if (y1[0]=='-'):
           yVal = (int(y1[1])*10 + int(y1[2]))*(-1)

        else:
            yVal = int(y1[0])*100 + int(y1[1]) *10 + int(y1[2])

    elif (len(y1) == 4):
        if (y1[0]=='-'):
           yVal = (int(y1[1])*100 + int(y1[2])*10 + int(y1[3]))*(-1)

        else:
            yVal = int(y1[0])*1000 + int(y1[1])*100 + int(y1[2])*10 + int(y1[3])





    if (len(angle1) == 1):
       angleVal = int(angle1[0])


    elif (len(angle1) == 2):
        if (angle1[0] == '-'):
           angleVal = int(angle1[1])*(-1)

        else:
            angleVal = int(angle1[0])*10 + int(angle1[1])


    elif (len(angle1) == 3):
        if (angle1[0]=='-'):
           angleVal = (int(angle1[1])*10 + int(angle1[2]))*(-1)

        else:
            angleVal = int(angle1[0])*100 + int(angle1[1])*10 + int(angle1[2])


    elif (len(angle1) == 4):
        if (angle1[0]=='-'):
           angleVal = (int(angle1[1])*100 + int(angle1[2])*10 + int(angle1[3]))*(-1)

        else:
            angleVal = int(angle1[0])*1000 + int(angle1[1])*100 + int(angle1[2])*10 + int(angle1[3])


    return xVal, yVal, angleVal



#get the initial position of the robot by reading the first waypoint of the input file

argNum = len(sys.argv)

if (argNum == 2):

     print("STARTED")

else:

     print ("no file specified")
     exit(1)


initialPosition = open(sys.argv[1], 'r').readline().rstrip()
secondPos  = linecache.getline(sys.argv[1], 2)


currentCoord = convertCoord(list(cutCoord(initialPosition)))
nextCoord = convertCoord(list(cutCoord(secondPos)))

print(currentCoord)
print(nextCoord)




num_lines = sum(1 for line in open(sys.argv[1], 'r'))

waypointsList = []

for i in range(1,num_lines+1):
    pos = linecache.getline(sys.argv[1],i)
    i= convertCoord(list(cutCoord(pos)))
    waypointsList.append(i)



# maintenant je dois resoudre l'equation pour savoir quels sont les params a rentrer pour aller au second waypoint
