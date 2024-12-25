# Python script for day 2
file = open('input.txt','r')
total = 0
for line in file:
    levels=line.split()
    safe=True
    series=0
    for i in range(len(levels)-1):
        diff=int(levels[i])-int(levels[i+1])
        if abs(diff)>3 or abs(diff) <1:
            safe=False
            break
        if series:
            if series < 0 and diff > 0 or diff < 0 and series > 0:
                safe=False
                break
            series += diff
            continue
        series = diff
    if safe:
        total+=1
print(total)


#part 2
file = open('input.txt','r')
total = 0
for line in file:
    levels=line.split()
    levels=list(map(int,levels))
    safe=True
    series=0
    diffs=[]
    for i in range(len(levels)-1):
        diffs.append(levels[i]-levels[i+1])
        if abs(diffs[i])>3 or abs(diffs[i]) <1:
            safe=False
            break
        if series:
            if series < 0 and diffs[i] > 0 or diffs[i] < 0 and series > 0:
                safe=False
                break
            series += diffs[i]
            continue
        series = diffs[i]
    if safe:
        total+=1
        continue
    for i in range(len(levels)):
        safe2=True
        diffs2=[]
        series2=0
        levels2=levels[:i]+levels[i+1:]
        for j in range(len(levels2)-1):
            diffs2.append(levels2[j]-levels2[j+1])
            if abs(diffs2[j])>3 or abs(diffs2[j]) <1:
                safe2=False
                break
            if series2:
                if series2 < 0 and diffs2[j] > 0 or diffs2[j] < 0 and series2 > 0:
                    safe2=False
                    break
                series2 += diffs2[j]
                continue
            series2 = diffs2[j]
        if safe2:
            total+=1
            break
print(total)