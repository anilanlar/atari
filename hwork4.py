lengthofasteroids= int(input())
heightofasteroids= int(input())
distancebetweenspaceshipandasteroids= int(input())

allasteroids=[]

def printthescene():
    for m in allasteroids:
        for h in m:
            print(h, end='')
        print()
    print(72*'-')



# INITIAL POSITIONS OF ASTEROIDS
for i in range(heightofasteroids):
    eachasteroidsegment=[]
    for j in range(lengthofasteroids):
        eachasteroidsegment.append('*')
    allasteroids.append(eachasteroidsegment)

# IMPLEMENTING EMPTY LISTS

for i in range(distancebetweenspaceshipandasteroids):
    eachspacesegment=[]
    for j in range(lengthofasteroids):
        eachspacesegment.append(' ')
    allasteroids.append(eachspacesegment)

# SPACESHIP CONTROL LIST
spaceshipcontrollist = []
for i in range(lengthofasteroids):
    spaceshipcontrollist.append(' ')
allasteroids.append(spaceshipcontrollist)

# INSERTING THE SPACESHIP INTO THE SPACESHIP CONTROL LIST
if lengthofasteroids%2!=0:
    indexofspaceship= (lengthofasteroids//2)
else:
    indexofspaceship= (lengthofasteroids//2)-1

if not (heightofasteroids==0 or lengthofasteroids==0):
    spaceshipcontrollist[indexofspaceship]='@'
    printthescene()

if heightofasteroids==0 or lengthofasteroids==0:
    print('YOU WON!')
    for i in range(distancebetweenspaceshipandasteroids):
        print()
    print('@')
    print(72*'-')



timer=0

while lengthofasteroids!=0 and heightofasteroids!=0:
    # DANGEROUS INPUTS

    action= input('Choose your action!')
    action=action.lower()
    # TIMER IS INCREMENTED BY 1
    timer += 1

    if action=='exit':
        printthescene()
        break

    if action=='right':
        if indexofspaceship<lengthofasteroids-1:
            spaceshipcontrollist[indexofspaceship] = ' '
            indexofspaceship += 1
            spaceshipcontrollist[indexofspaceship] = '@'

    if action == 'left':
        if indexofspaceship > 0:
            spaceshipcontrollist[indexofspaceship]=' '
            indexofspaceship -= 1
            spaceshipcontrollist[indexofspaceship]='@'

    if action=='fire':
        heightplusspace = heightofasteroids + distancebetweenspaceshipandasteroids
        for i in range(0,heightplusspace):
            if allasteroids[heightplusspace-1-i][indexofspaceship]!='*':
                allasteroids[heightplusspace-1-i][indexofspaceship] = '|'
                printthescene()
                allasteroids[heightplusspace-1-i][indexofspaceship]=' '

            elif allasteroids[heightplusspace-1-i][indexofspaceship]=='*':
                allasteroids[heightplusspace-1-i][indexofspaceship]= ' '
                break

    # CHECKING IF THE USER HAS WON AFTER THE SHOT
    asteroidcounter=0
    for eachlist in allasteroids:
        for i in eachlist:
            if i=='*':
                asteroidcounter+=1
    if asteroidcounter==0:
        print('YOU WON!')
        printthescene()
        break


    # CHECKING WHETHER OR NOT TO SLIDE ASTEROIDS
    if timer % 5 == 0 and timer != 0:
        newbornlist = [' ' for each in range(lengthofasteroids)]
        allasteroids.insert(0, newbornlist)
        if allasteroids[-2].count('*') == 0:
            allasteroids.pop(-2)
        else:
            print('GAME OVER')
            printthescene()
            break
        #     GAME OVER


    printthescene()