# Python script for day 8
file = open('input.txt','r')
map=[]
for line in file:
    row=[]
    for c in line:
        if c!="\n":
            row.append(c)
    map.append(row)
antenna=dict()
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] != "." and map[row][col] != "#":
            if map[row][col] not in antenna:
                antenna[map[row][col]]=[]
            antenna[map[row][col]].append((row,col))
antinode_loc=[]
for frequency in antenna:
    possibilities=antenna[frequency]
    for first in range(len(possibilities)-1):
        for second in range(first +1,len(possibilities)):
            dist=(possibilities[second][0]-possibilities[first][0],possibilities[second][1]-possibilities[first][1])
            antinode_pair=[(possibilities[first][0]-dist[0],possibilities[first][1]-dist[1]),(possibilities[second][0]+dist[0],possibilities[second][1]+dist[1])]
            for antinode in antinode_pair:
                if antinode[0]>-1 and antinode[0]<len(map) and antinode[1]>-1 and antinode[1]<len(map[0]):
                    if antinode not in antinode_loc:
                        antinode_loc.append(antinode)
print(len(antinode_loc))
#part 2
file = open('input.txt','r')
map=[]
for line in file:
    row=[]
    for c in line:
        if c!="\n":
            row.append(c)
    map.append(row)
antenna=dict()
for row in range(len(map)):
    for col in range(len(map[0])):
        if map[row][col] != "." and map[row][col] != "#":
            if map[row][col] not in antenna:
                antenna[map[row][col]]=[]
            antenna[map[row][col]].append((row,col))
antinode_loc=[]
for frequency in antenna:
    possibilities=antenna[frequency]
    for first in range(len(possibilities)-1):
        for second in range(first +1,len(possibilities)):
            dist=(possibilities[second][0]-possibilities[first][0],possibilities[second][1]-possibilities[first][1])
            above=[possibilities[first]]
            while above[-1][0]>-1:
                above.append((above[-1][0]-dist[0],above[-1][1]-dist[1]))
            below=[possibilities[second]]
            while below[-1][0]<len(map):
                below.append((below[-1][0]+dist[0],below[-1][1]+dist[1]))
            antinode_list=above+below
            for antinode in antinode_list:
                if antinode[0]>-1 and antinode[0]<len(map) and antinode[1]>-1 and antinode[1]<len(map[0]):
                    if antinode not in antinode_loc:
                        antinode_loc.append(antinode)
print(len(antinode_loc))