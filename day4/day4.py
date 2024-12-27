# Python script for day 4
file = open('input.txt','r')
data=[[i for i in line if i!="\n"]for line in file]
total=0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j]=="X":
            if "".join(data[i][j:j+4])=="XMAS":
                total+=1
            if "".join(data[i][j-3:j+1]) == "SAMX":
                total+=1
            if i>=3:
                if "".join(data[i-3][j]+data[i-2][j]+data[i-1][j]+data[i][j])=="SAMX":
                    total+=1
                if j>=3:
                    if "".join(data[i-3][j-3]+data[i-2][j-2]+data[i-1][j-1]+data[i][j])=="SAMX":
                        total+=1
                if j<len(data)-3:
                    if "".join(data[i-3][j+3]+data[i-2][j+2]+data[i-1][j+1]+data[i][j])=="SAMX":
                        total+=1
            if i<len(data)-3:
                if "".join(data[i][j]+data[i+1][j]+data[i+2][j]+data[i+3][j])=="XMAS":
                    total+=1
                if j>=3:
                    if "".join(data[i][j]+data[i+1][j-1]+data[i+2][j-2]+data[i+3][j-3])=="XMAS":
                        total+=1
                if j<len(data[0])-3:
                    if "".join(data[i][j]+data[i+1][j+1]+data[i+2][j+2]+data[i+3][j+3])=="XMAS":
                        total+=1
print(total)
#part 2 (problem is unclear but letters have to be on the same side)
file = open('input.txt','r')
data=[[i for i in line if i!="\n"]for line in file]
total=0
for i in range(1,len(data)-1):
    for j in range(1,len(data[0])-1):
        if data[i][j]=="A":
            corners=data[i-1][j-1]+data[i-1][j+1]+data[i+1][j-1]+data[i+1][j+1]
            if corners.count("S")==2 and corners.count("M") ==2:
                total+=1
                if data[i-1][j-1]==data[i+1][j+1]:
                    total-=1
print(total)
