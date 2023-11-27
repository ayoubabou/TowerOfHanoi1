numDisks = int(input("Enter how many disks you want : "))
diskPos = {}
diskLastPos = {}
for i in range(numDisks):
    diskPos[i+1] = 1
    diskLastPos[i+1] = 0
towers = [list(range(1,numDisks+1))[::-1], [], []]
moves = 0
lastDiskMoved = 0
print(towers)

def moveFunc(disk,nextTower):
    global diskPos, diskLastPos, towers, moves, lastDiskMoved
    print("Disk",disk,"moves from Tower",diskPos[disk],"to Tower",nextTower)
    towers[diskPos[disk]-1].pop()
    lastDiskMoved = disk
    diskLastPos[disk] = diskPos[disk]
    diskPos[disk] = nextTower
    moves += 1
    towers[nextTower-1].append(disk)
    print(towers)

def otherTowers(towPos):
    return [pos for pos in range(1,4) if not pos in towPos]

def diskCanMove(disk):
    if (disk != lastDiskMoved):
        if ((len(towers[0])>0 and towers[0][-1]==disk) or (len(towers[1])>0 and towers[1][-1]==disk) or (len(towers[2])>0 and towers[2][-1]==disk)):
            if [] in towers:
                return True
            elif((len(towers[otherTowers([diskPos[disk]])[0]-1])>0 and towers[otherTowers([diskPos[disk]])[0]-1][-1]>disk) or ((len(towers[otherTowers([diskPos[disk]])[1]-1])>0 and towers[otherTowers([diskPos[disk]])[1]-1][-1]>disk))):
                return True
    return False
                
def towerOfHanoi():
    diskToMove = 1
    if(numDisks%2==1):
        moveFunc(diskToMove,3)
    else:
        moveFunc(diskToMove,2)
    diskToMove += 1
    while(len(towers[2])<numDisks):
        if(diskCanMove(diskToMove)):
            if (diskLastPos[diskToMove] == 0):
                for tower in towers:
                    if (len(tower)==0 or ((not (diskToMove in tower)) and tower[-1]>diskToMove)):
                        moveFunc(diskToMove,towers.index(tower)+1)
            else:
                moveFunc(diskToMove,otherTowers([diskPos[diskToMove],diskLastPos[diskToMove]])[0])
        else:
            if(diskCanMove(1)):
                diskToMove = 1
            else:
                while(not diskCanMove(diskToMove) and diskToMove<=numDisks):
                    if (diskToMove == numDisks):
                        diskToMove = 1
                        break
                    diskToMove += 1
    print("The number of moves are",moves,"moves")
    
towerOfHanoi()










