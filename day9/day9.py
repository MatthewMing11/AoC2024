# Python script for day 9
# file = open('input.txt','r').read()
# file=file[:len(file)-1]
# id=0
# liststr=[]
# freespace=False
# for c in file:
    # occurrence=int(c)
    # if not freespace:
        # for i in range(occurrence):
            # liststr.append(id)
        # id+=1
        # freespace=True
    # else:
        # for i in range(occurrence):
            # liststr.append(".")
        # freespace=False
# while "." in liststr:
    # if liststr[-1]==".":
        # while liststr[-1]==".":
            # liststr.pop()
    # index=liststr.index(".")
    # liststr[index]=liststr[-1]
    # liststr.pop()
# total=0
# for pos in range(len(liststr)):
#     # total+=pos*liststr[pos]
# print(total)
#part 2
file = open('input.txt','r').read()
file=file[:len(file)-1]
file=list(file)
id=0
liststr=[]
filespace=[]
free=[]
for c in range(len(file)):
    if c%2==0:
        filespace.append(c)
        group=[]
        for i in range(int(file[c])):
            group.append(id)
        id+=1
        liststr.append(group)
    else:
        free.append(c)
        group=[]
        for i in range(int(file[c])):
            group.append(".")
        liststr.append(group)
# print(filespace)
# print(liststr)
filespace=filespace[::-1]
for whole in filespace:
    for spot in free:
        if file[whole]<= file[spot] and spot <whole:
            diff=int(file[spot])-int(file[whole])
            file[spot]=str(diff)
            if diff==0:
                free.remove(spot)
            index=liststr[spot].index(".")
            for i in range(len(liststr[whole])):
                liststr[spot][i+index]=liststr[whole][i]
            file[whole]="0"
            liststr[whole]=["." for _ in range(len(liststr[whole]))]
            break
string=[]
for sublist in liststr:
    string+=sublist
total=0
for c in range(len(string)):
    if string[c]!=".":
        total+=c*string[c]
print(total)