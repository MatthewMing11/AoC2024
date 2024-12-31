# Python script for day 6
file = open('input.txt','r')
directions=["^",">","v","<",]
updates=[(-1,0),(0,1),(1,0),(0,-1)]
map=[]
obstacles=[]
position=()
direction=0
for line in file:
    row=[]
    for c in line:
        if c!="\n":
            row.append(c)
    map.append(row)
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] == "#":
            obstacles.append((row,col))
        if map[row][col] in directions:
            position=(row,col)
            direction=directions.index(map[row][col])
while position[0]>-1 and position[1]>-1 and position[0]<len(map) and position[1]<len(map[0]):
    if map[position[0]][position[1]]!="X":
        map[position[0]][position[1]]="X"
    newpos = tuple(sum(x) for x in zip(position,updates[direction]))
    if newpos[0]<0 or newpos[1]<0 or newpos[0]>=len(map) or newpos[1]>=len(map[0]):
        break
    if map[newpos[0]][newpos[1]]=="#":
        direction=(direction+1)%4
        continue
    position=newpos
    map[newpos[0]][newpos[1]]=directions[direction]
total=0
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col]=="X":
            total+=1
print(total)
#part 2
file = open('input.txt','r')
directions=["^",">","v","<",]
updates=[(-1,0),(0,1),(1,0),(0,-1)]
map=[]
obstacles=[]
position=()
direction=0
for line in file:
    row=[]
    for c in line:
        if c!="\n":
            row.append(c)
    map.append(row)
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] == "#":
            obstacles.append((row,col))
        if map[row][col] in directions:
            position=(row,col)
            direction=directions.index(map[row][col])
originalmap=[row[:] for row in map]
originalpos = position
originaldir = direction
total=0
for row in range(len(map)):
    for col in range(len(map[0])):
        if originalmap[row][col]!="#":
            map=[r[:] for r in originalmap]
            map[row][col]="#"
            position = originalpos
            direction = originaldir
            passedob=[]
            while position[0]>-1 and position[1]>-1 and position[0]<len(map) and position[1]<len(map[0]):
                if map[position[0]][position[1]]!="X":
                    map[position[0]][position[1]]="X"
                newpos = tuple(sum(x) for x in zip(position,updates[direction]))
                if newpos[0]<0 or newpos[1]<0 or newpos[0]>=len(map) or newpos[1]>=len(map[0]):
                    break
                if map[newpos[0]][newpos[1]]=="#":
                    if (newpos,direction) in passedob:
                        total+=1
                        break
                    passedob.append((newpos,direction))
                    direction=(direction+1)%4
                    continue
                position=newpos
                map[newpos[0]][newpos[1]]=directions[direction]
print(total)