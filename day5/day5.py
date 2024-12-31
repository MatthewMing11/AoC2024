# Python script for day 5
file = open('input.txt','r')
rules =True
ordering=dict()
correct=[]
for line in file:
    if line=="\n":
        rules=False
        continue
    if rules:
        first,second=line.split("|")
        second= second[:len(second)-1]
        if first not in ordering:
            ordering[first]=[];
        ordering[first].append(second)
    else:
        updates=line.split(",")
        updates[-1]=updates[-1][:len(updates[-1])-1]
        right=True
        for i in range(len(updates)-1):
            for j in range(i+1, len(updates)):
                if updates[j] not in ordering[updates[i]]:
                    right=False
                    break
            if not right:
                break
        if right:
            correct.append(updates)
total=0
for coupdates in correct:
    total+=int(coupdates[int(len(coupdates)/2)])
print(total)
#part 2
file = open('input.txt','r')
rules =True
ordering=dict()
correct=[]
for line in file:
    if line=="\n":
        rules=False
        continue
    if rules:
        first,second=line.split("|")
        second= second[:len(second)-1]
        if first not in ordering:
            ordering[first]=[];
        ordering[first].append(second)
    else:
        updates=line.split(",")
        updates[-1]=updates[-1][:len(updates[-1])-1]
        right=True
        for i in range(len(updates)-1):
            for j in range(i+1, len(updates)):
                if updates[j] not in ordering[updates[i]]:
                    right=False
                    break
            if not right:
                break
        if not right:
            common=[]
            for i in range(len(updates)):
                common.append(len([x for x in updates if x in ordering[updates[i]]]))
            new_updates=[val for _,val in reversed(sorted(zip(common,updates)))]
            correct.append(new_updates)
total=0
for coupdates in correct:
    total+=int(coupdates[int(len(coupdates)/2)])
print(total)