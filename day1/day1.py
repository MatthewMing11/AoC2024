# Python script for day 1
file = open("input.txt","r")
total = 0
alist=[]
blist=[]
for line in file:
    a,b=line.split()
    alist.append(a)
    blist.append(b)
alist=sorted(alist)
blist=sorted(blist)
for i in range(1000):
    total+=abs(int(alist[i])-int(blist[i]))
print(total)

