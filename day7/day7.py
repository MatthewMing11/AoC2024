# Python script for day 7
file = open('input.txt','r')
total=0
for line in file:
    if line[-1]=="\n":
        line = line[:len(line)-1]
    equation=line.split(":")
    operands=equation[1].split()
    result=int(equation[0])
    from itertools import product
    operatorcombo= product('01',repeat=len(operands)-1)
    valid=False
    first=int(operands[0])
    for combo in operatorcombo:
        current=first
        for i in range(1,len(operands)):
            if combo[i-1]=="0":
                current+=int(operands[i])
            elif combo[i-1]=="1":
                current*=int(operands[i])
        if current==result:
            valid=True
            break
    if valid:
        total+=result
print(total)
#part 2
file = open('input.txt','r')
total=0
for line in file:
    if line[-1]=="\n":
        line = line[:len(line)-1]
    equation=line.split(":")
    operands=equation[1].split()
    result=int(equation[0])
    from itertools import product
    operatorcombo= product('012',repeat=len(operands)-1)
    valid=False
    first=int(operands[0])
    for combo in operatorcombo:
        current=first
        for i in range(1,len(operands)):
            if combo[i-1]=="0":
                current+=int(operands[i])
            elif combo[i-1]=="1":
                current*=int(operands[i])
            elif combo[i-1]=="2":
                current=int(str(current) + operands[i])
        if current==result:
            valid=True
            break
    if valid:
        total+=result
print(total)